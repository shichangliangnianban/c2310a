# 1.什么是正则化？都有哪些方式？有什么区别

# 设计机器学习算法的时候，我们不仅要求训练集合上误差小，而且要求在其他样本的预测能力（泛化能力）强，许多机器学习算法采用相关的策略来减小误差，这些策略称为正则化。
# L1正则化；L2正则化
# L1正则化：通过向损失函数添加权重向量的元素绝对值之和来实施，倾向于产生稀疏的权重矩阵，即某些权重会变成零。
# L2正则化：通过增加权重向量元素的平方和来施加惩罚，它倾向于让权重分布在各个特征之间，而不是完全消除某些特征的权重。
# 2.什么是dropout？
# 是一种用于深度学习模型中防止过拟合的技术
# 3.dropout有哪几种实现方式？
# 随即丢弃：在每次迭代训练时，会随机选择网络中的一些神经元并将其临时隐藏或“丢弃”。这意味着这些神经元在当前批次的训练中不会参与前向传播和反向传播过程。
# 丢失率设置：Dropout的一个重要参数是丢失率，它控制着每次迭代中被丢弃的神经元的比例。这个比例可以根据模型的需要进行调整，以找到最佳的正则化效果。
# 变种应用：Dropout不仅适用于普通的全连接层，还有针对卷积神经网络（CNN）和循环神经网络（RNN）的特殊变种。
# 4.什么是早停法，什么情况使用早停法？
# 早停法是一种用于防止机器学习模型过拟合的技术，通常在验证集的性能不再提升甚至开始下降时使用。
# 5.BN是什么意思？解决了什么问题？怎么实现使用pytorch？
# BN是Batch Normalization的缩写，即批量归一化。
# 每一层的输入进行归一化处理，以稳定网络的学习过程
#
# import torch.nn as nn
#
# # 假设有一个输入特征为64的卷积层
# conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)
#
# # 添加批量归一化层
# bn = nn.BatchNorm2d(64)
#
# # 在训练过程中使用bn
# input_tensor = torch.randn(10, 3, 32, 32)  # 假设有10个样本，每个样本的尺寸为3x32x32
# output = conv(input_tensor)
# normalized_output = bn(output)
#
# 6.介绍RNN的使用场景
# 主要用于处理序列数据，如文本、语音和时间序列等。
# 7.RNN的公式
# hj=tanh(Uxj+Whj-1+b)
# 8.RNN存在什么缺陷？这些缺陷是如何导致的？
# 梯度消失：
# 由于反向传播的时间链较长，梯度可能会随着时间步的增加而指数级减小，导致网络难以学习到长期的依赖关系
# 计算复杂度高：
# 由于引入了门控机制和记忆单元，模型的参数量和计算量都会显著增加。
# 难以解释性：
# LSTM网络中的门控结构和复杂的记忆单元使得网络的决策过程相对难以解释和理解，这对于需要模型透明度的应用场景来说可能是一个问题
#
# 9.LSTM有哪些门？
# 遗忘门、输入门和输出门