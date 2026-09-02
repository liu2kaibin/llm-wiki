---
type: concept
domain: 存储
tags:
  - 存储
status: seed
created: 2026-09-02
source: "Oracle 内部资料（SharePoint 剪藏，2026-09-02）"
---
# ZFS 存储系统

> [!abstract] 一体化企业存储阵列——用 DRAM 缓存和全闪存把 IO 挡在内存里，还内置数据库感知的 IO 优先级调度
> （先把剪藏里的话变成你自己的：一体化企业存储阵列——用 DRAM 缓存和全闪存把 IO 挡在内存里，还内置数据库感知的 IO 优先级调度。）

## 它解决什么问题

## 工作原理
- DRAM 缓存吸收存储 IO
- 全闪存配置 → 性能；磁盘配置 → 成本
- 可伸缩软件消除 IO 瓶颈
- 数据库集成功能：自动对数据库 IO 排优先级

## 直觉类比

## 关系
- **相关**：[[Buffer Pool]]（同样是「大内存缓存挡在前」的思路）、[[WAL]]
- **对比**：

## 常见误解
- ZFS（开源文件系统）≠ Oracle ZFS 存储一体机（基于 ZFS 的商业产品）

## 出处
- Oracle 内部 SharePoint 页面（2026-09-02 剪藏；原文在本地 Clippings/，不入公开库）
