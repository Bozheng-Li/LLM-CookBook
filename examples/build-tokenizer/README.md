# 手写 BPE Tokenizer

对应正文：[第 15 章 · 从零实现 Tokenizer](../../pages/15-practice/build-tokenizer.html)

**零依赖**，只用 Python 标准库。没有网络请求，没有预训练模型下载。

## 跑起来

```bash
cd examples/build-tokenizer
python train.py                    # 默认语料，词表 1024
python test_bpe.py                 # 自检（也可以 python -m pytest test_bpe.py）
```

预期输出（约 2 秒）：

```
语料 corpus.txt：4126 字符，800 个词片
词表大小      1024
原文字节      5684
token 数      1888
压缩率        3.01 字节/token
往返一致      ✓

编码示例：
  'hello world'    -> 7 tokens ['he', 'll', 'o', ' w', 'or', 'l', 'd']
  '大模型'            -> 2 tokens ['大', '模型']
  ' the model'     -> 2 tokens [' the', ' model']
```

## 代码地图

| 文件 | 作用 |
| --- | --- |
| `bpe.py` | 全部核心逻辑：预分词、训练、编码、解码、存取 |
| `train.py` | CLI，训练并打印压缩率与最长 token |
| `test_bpe.py` | 9 项自检，覆盖确定性、无损往返、合并语义 |
| `data/corpus.txt` | 4 KB 中英混排语料，自撰，无版权问题 |

## 三个值得自己验证的点

**1. 语料太小会让 BPE 过拟合。** 跑完默认配置看「最长 10 个 token」，你会看到
`'化则告诉模型在两个都合理的回答之间应'` 这种半句话被压成一个 token。因为语料里
这句话只出现一次，它内部每个 pair 的频次都相等且没有竞争者，于是被一路合并到底。
真实语料上不会这样——常见片段的频次会远高于长句。想复现这个对比，把
`data/corpus.txt` 换成任意几百 KB 的文本再跑一次。

**2. 字节级词表没有 UNK。** `test_unknown_bytes_are_invocab` 用一个只有 256 个
基础字节、零合并规则的 tokenizer 编码 emoji，仍然能无损还原。代价是压缩率退化到
1 字节/token。词表大小买的就是压缩率。

**3. 训练必须是确定性的。** `test_train_is_deterministic` 检查同一份语料两次训练
得到完全一样的合并序列。实现上靠 `max(stats.items(), key=lambda kv: (kv[1], kv[0]))`
——频次相同时用 pair 本身的 id 做二级排序。少了这一句，Python 字典迭代顺序的
微小变化就会让词表漂移，而词表漂移意味着已经训好的模型全部作废。

## 换成生产实现

这份代码是为了讲清楚机制，不是为了快。真实项目请用 Hugging Face `tokenizers`
（Rust 实现，训练快两三个数量级，且支持 special token、normalizer、
byte-level alphabet 等本例省略的部分）：

```python
from tokenizers import Tokenizer, models, trainers, pre_tokenizers, decoders

tok = Tokenizer(models.BPE())
tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
tok.decoder = decoders.ByteLevel()
tok.train(["data/corpus.txt"], trainers.BpeTrainer(vocab_size=1024))
```

两者的 `merges` 语义一致，可以互相对照。差异主要在预分词正则和 special token 处理。
