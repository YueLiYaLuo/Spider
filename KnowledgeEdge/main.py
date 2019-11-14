#主方法，演示用

from spider.KnowledgeEdge import GetEntity as ge
getEntity = ge.GetEntity()
# getEntity.get_EntityName("https://en.wikipedia.org/wiki/Data_structure")
# 1.获取概念及概念详细信息页面链接
getEntity.get_Info()
# 2.获取概念的具体表述内容
# 3.数据缺失处理并实现中文转换