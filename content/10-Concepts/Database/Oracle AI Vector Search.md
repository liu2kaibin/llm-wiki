---
type: concept
domain: database
tags:
  - database
  - llm
status: seed
created: 2026-09-02
source: "https://oracle-base.com/articles/23/ai-vector-search-23"
---
# Oracle AI Vector Search

> [!abstract] TL;DR 一句话直觉
> Oracle 23ai 把向量变成一等公民：`VECTOR` 直接当列类型，SQL 里就能做语义相似度检索——不用外挂向量库，业务数据和语义向量同库同事务。【读一遍，改成你的话】

## 它解决什么问题
- 传统做法：结构化数据在关系库、语义向量在专用向量库（Milvus/pgvector 等），两套系统双写、JOIN 靠应用层。
- 23ai 起内核原生支持，语义检索和关系查询在同一个库、同一条 SQL 里完成。

## 工作原理
1. **选模型**：下载 embedding 模型（如 all_MiniLM_L12_v2）的 ONNX 文件；
2. **模型入库**：用 `DBMS_VECTOR` 包把 ONNX 模型加载进数据库；
3. **生成向量**：`VECTOR_EMBEDDING('文本')` 函数生成向量，表的向量列用新数据类型 `VECTOR(*,*)`；
4. **语义检索**：`VECTOR_DISTANCE(v1, v2)` 计算距离，`ORDER BY` 距离即最近邻搜索；
5. **可选加速**：建向量索引（HNSW/IVF 类），需先设置 `VECTOR_MEMORY_SIZE` 参数。

## 直觉类比
【留给你：比如"以前要雇个翻译把外语资料搬进自家图书馆，现在图书馆自己会读外语了"之类的类比】

## 关系
- **相关**：[[向量数据库]]（对比：外挂向量库 vs 内核内置）、[[Embedding]]、[[RAG]]（这就是 RAG 存储层的又一个选项）
- **对比**：pgvector / Milvus / Elasticsearch——外挂方案的取舍是灵活性与规模 vs 一体化与事务一致性

## 常见误解
- 以为要装插件或外挂组件——23ai 起是内核原生功能；
- 向量索引不是免费的：`VECTOR_MEMORY_SIZE` 要吃实打实的内存。

## 出处
- oracle-base.com: [AI Vector Search in Oracle Database 23ai/26ai](https://oracle-base.com/articles/23/ai-vector-search-23)，2026-09-02 剪藏
