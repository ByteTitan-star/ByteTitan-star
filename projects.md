# 🚀 Projects

Detailed notes on the things I've built. The short versions live on my [profile](https://github.com/ByteTitan-star).

---

## 🎮 GameForge — AI-powered Browser Game Studio

**浏览器里的 AI 游戏工作室**

[![GitHub](https://img.shields.io/badge/Repo-GameForge--Copilot-181717?style=flat-square&logo=github)](https://github.com/ByteTitan-star/GameForge-Copilot)
[![Live Demo](https://img.shields.io/badge/Live-Demo-00BFA5?style=flat-square)](http://62.234.65.18/agent)

An AI-assisted browser game studio that turns a natural-language gameplay idea into a playable browser game through multi-round dialogue, structured planning, human confirmation, and generation with live progress. Supports delivery targets such as React and other modern web frameworks; creators can playtest in the browser, manage versions, meter tokens, and download or publish builds without writing code.

> 面向浏览器游戏的 AI 辅助创作工作区：从自然语言玩法描述出发，经多轮对话、结构化策划、人工确认与游戏生成，得到可直接试玩的浏览器游戏作品，支持 React 等现代前端框架交付，并完成版本管理、Token 计量、下载与发布。

**Flow:** `IDEA → PLAN → CONFIRM → GENERATE → PLAY`

**Stack:** React 19 · Harness · LangGraph · Langfuse · Sandbox · FastAPI · Redis · RabbitMQ · SSE · Agent

---

## 🤖 CodingKing — Autonomous Coding Agent

[![GitHub](https://img.shields.io/badge/Repo-CodingKing-181717?style=flat-square&logo=github)](https://github.com/ByteTitan-star/CodingKing)

An autonomous coding agent with a self-built **ReAct + Reflection loop**, a custom **tool protocol**, repository-aware context, **Docker sandbox execution**, test-driven validation, and automatic repair. Supports configurable OpenAI-compatible models, CLI/Web workflows, Git diff tracking, and measurable coding-task evaluation.

---

## 🎬 VideoGen-Agent — Multi-Stage AI Video Generation & Evaluation

**多阶段 AI 视频生成与自动评测 Agent**

[![GitHub](https://img.shields.io/badge/Repo-VideoGen--Agent-181717?style=flat-square&logo=github)](https://github.com/ByteTitan-star/VideoGen-Agent)

An end-to-end video-generation agent workflow built on **LangGraph**, decomposing a natural-language idea into `Script Generation → Storyboard → Shot Planning → Video Generation → Evaluation → Post-processing`. Integrates Seedance / Kling and other video models behind a **unified model adapter with dynamic routing**, supporting T2V / I2V async task scheduling, failure retry, and model degradation.

---

## 📄 PaperDistiller — Multi-Agent Research Workspace

**多智能体科研工作台**

[![GitHub](https://img.shields.io/badge/Repo-Agent__PaperDistiller-181717?style=flat-square&logo=github)](https://github.com/ByteTitan-star/Agent_PaperDistiller)

A unified research workspace for paper reading and analysis: PDF parsing, layout-aware structured extraction, RAG question answering, novelty analysis, bilingual translation, and collaborative agents — connected by task orchestration, streaming feedback, and knowledge-base management, from paper import to insight capture.

> 围绕论文阅读与科研分析场景，把 PDF 解析、结构化信息抽取、RAG 检索问答、创新点分析、双语翻译和多智能体协作整合到统一工作流中，串联从论文导入、内容理解到观点沉淀的完整过程。

**Stack:** Vue 3 · FastAPI · RAG · LangGraph · ToT · SSE · ChromaDB · BM25

---

## 💬 SoulMate — Personalized AI Companion Platform

**个性化 AI 伴侣平台**

[![GitHub](https://img.shields.io/badge/Repo-Agent__SoulMate-181717?style=flat-square&logo=github)](https://github.com/ByteTitan-star/Agent_SoulMate)

A full-stack AI companion driven by **local LLMs (Ollama)** for long-term personalized interaction: user-defined personas, private knowledge binding, short/long-term conversational memory, tool use, and scalable vector retrieval (Milvus), with real-time voice chat. React + Django.

---

## 🔧 Smaller Pieces

- [open_assisant](https://github.com/ByteTitan-star/open_assisant) — turn PDF papers into structured, translated, personalized reading summaries
- [generalQA](https://github.com/ByteTitan-star/generalQA) — GeneralQA & DeepResearch experiments
- [md2pdf](https://github.com/ByteTitan-star/md2pdf) — Markdown → PDF microservice
- [upload_File](https://github.com/ByteTitan-star/upload_File) — file upload service returning complete URL after POST
