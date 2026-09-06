import os

path = r"D:/agent-cookbook/chapters/ch092.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="theory-epistemology-summary">系统论的认识论启示：自组织、稳态与终极生命体</h2>
    <p>回顾控制论与系统论这百年来走过的壮丽学术思想史，我们发现：从维纳对动物神经与蒸汽调速器负反馈机制的统一抽象，到阿什比从信息论硬核约束中提炼出的“唯有多样性才能吸收多样性”铁律；从普里戈金以耗散结构论破译“生命以负熵为食”的物理密码，再到哈肯役使原理揭示微观快变量如何自发臣服于宏观序参数的深刻辩证法——这一整套思想体系，绝非陈旧的故纸堆，而是为当今前沿人工智能智能体系统量身定制的最深刻的工程与哲学武器。</p>
    
    <p>当一个智能体不再仅仅被视为一个静态的矩阵乘法计算器，而是被置于动态演化的环境激流之中时，它便成为了一个货真价实的数字生命体。唯有深刻领会控制论中的闭环抑制自激、自适应抵御扰动、以及持续从客观真实世界吸纳负熵以抗击内部混沌退化的物理真理，我们才能在构建千亿参数、千万步长时程超级自主智能体的伟大征途中，始终立于不败之地。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemological summary section")
else:
    print("Target not found")
