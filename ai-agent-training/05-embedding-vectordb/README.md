# Module 05: Embedding和向量数据库

> 目标：理解向量化原理，掌握向量数据库使用，这是RAG的基础

## 🎯 学习目标

- [ ] 理解Embedding（嵌入）原理
- [ ] 掌握向量相似度计算
- [ ] 学会使用ChromaDB和FAISS
- [ ] 掌握语义搜索
- [ ] 理解混合检索

## 📊 练习列表（12题）

### Part 1: Embedding (4题)
- ex01_embedding_basics.py - Embedding原理
- ex02_openai_embeddings.py - OpenAI Embeddings
- ex03_local_embeddings.py - 本地Embedding模型
- ex04_embedding_comparison.py - Embedding对比

### Part 2: 向量数据库 (4题)
- ex05_chroma_basics.py - ChromaDB基础
- ex06_faiss_basics.py - FAISS基础
- ex07_similarity_search.py - 相似度搜索
- ex08_metadata_filtering.py - 元数据过滤

### Part 3: 高级检索 (4题)
- ex09_mmr.py - MMR检索
- ex10_hybrid_search.py - 混合检索
- ex11_reranking.py - 重排序
- ex12_vector_db_comparison.py - 向量库对比

## 🔥 核心概念

### Embedding是什么？

```python
# 文本 -> 向量
text = "Python是一种编程语言"
embedding = embedder.embed(text)
# embedding = [0.1, -0.3, 0.8, ...]  # 768维向量
```

### 向量相似度

```python
# 余弦相似度
similarity = cosine_similarity(vec1, vec2)
# 值越接近1，越相似
```

### 向量数据库

```python
# ChromaDB使用
vectorstore = Chroma.from_documents(documents, embeddings)
results = vectorstore.similarity_search("Python教程", k=3)
```

## ⏭️ 下一步

完成本模块后，可以开始构建RAG系统了！

