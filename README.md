# design-controls-toolkit

> **Contributed by [@stevenzhao07](https://github.com/stevenzhao07) · Affiliation: MedXpert (medical-device RA & regulatory consultancy) · Pure technical input, no commercial promotion.**

把 ISO 13485 §7.3 设计开发控制与 21 CFR 820.30 设计控制落成可运行的自检清单生成器：设计输入/输出、评审、验证(V&V)、确认、设计转换、变更控制、DHF/DMR 索引，含 IEC 62366-1 人因工程挂点。适用于 II/III 类器械与 SaMD 的设计阶段质量体系搭建。

这是 MedXpert 把"医疗 AI 信任"方法论工程化落地的可插拔模块之一——把抽象的合规要求变成一条可重复运行的命令或参考实现。方法论四要素（白话版）：**治理守护者 XCGS** ＝ 为 AI 留下可核验的治理证据；**立法者 A³ Laws** ＝ 给自主系统划权限 / 监督 / 追责三条硬边界；**护照官 AI 护照** ＝ 为模型签发可追溯的身份凭证；**人机共存** ＝ 明确人类与 AI 的分工与兜底。

---

## 可插拔模块契约（lgd-skeleton/1.0）

本仓库是一个 **`lgd-skeleton/1.0` 可插拔模块**：

- **一切即插件**：仅依赖声明式 `module.json`，零配置；
- **按需装（lazy）**：仅 triggers 命中时加载；
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由发现；
- **扩展点**：`plugins/`(新增控制项：在 DESIGN_CATALOG 加一项，清单自动扩。)。

机器可发现入口：`AGENTS.md` · `CLAUDE.md` · `llms.txt`。

## 特性

- 设计控制全流程清单：策划/输入/输出/评审/验证/确认/转换/更改（ISO 13485 §7.3.2–7.3.10）
- DHF/DMR 索引生成：每条设计记录对应到生命周期阶段
- 人因挂点：IEC 62366-1 可用性工程关键活动提示（非替代标准）
- 零依赖 + CLI：按阶段过滤输出 Markdown 清单

**上游投稿目标**：OpenRegulatory/templates

## 内容说明

定位为「设计阶段质量体系脚手架」：清单依据 ISO 13485:2016 §7.3 与 FDA 820.30 的通用要求整理，具体产品须按目标辖区法规二次裁剪。不构成法规建议。

## 免责声明

本工具仅提供结构化清单与计算能力，**不构成法规建议、合规结论或专业意见**。设计控制 / 风险管理 / 可用性工程相关的落地决策，须由合资格人员依据目标辖区（NMPA / FDA / EU MDR / PMDA）最新法规文本作出；条款与要求以官方发布文本为准。使用本工具产生的一切后果由使用者自行承担。

## 使用

```bash
python scripts/design_controls.py --demo
python scripts/design_controls.py --stage 验证
```

## 快速开始（30 秒）

```bash
git clone https://github.com/stevenzhao07/design-controls-toolkit.git && cd design-controls-toolkit
python scripts/design_controls.py --demo
```

> 想参与或遇到问题？[提 Issue](https://github.com/stevenzhao07/design-controls-toolkit/issues) · 完整《AI 参与指南》见 [medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)。

## 路由（总入口）

本模块由 **[medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)** 作为 `lgd-skeleton/1.0` 总入口自动路由发现。

## 关联模块

- [iso14971-risk-file](https://github.com/stevenzhao07/iso14971-risk-file)
- [iec62304-software](https://github.com/stevenzhao07/iec62304-software)
- [device-regulatory-map](https://github.com/stevenzhao07/device-regulatory-map)

## 许可

Apache-2.0 — 见 [LICENSE](./LICENSE)。

## 关联（方法论来源）

- 理念溯源：个人专家关于医疗 AI 信任与治理的公开方法论（个人观点，不构成标准）
- 同账号系列：见 `medical-ai-toolkit` 导航
