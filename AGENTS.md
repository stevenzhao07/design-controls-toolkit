# AGENTS.md · design-controls-toolkit

> 机器可发现入口（AI 编码代理 / Codex / Claude / Cursor）。单一事实源：本文件。

## 这是什么
把 ISO 13485 §7.3 设计开发控制与 21 CFR 820.30 设计控制落成可运行的自检清单生成器：设计输入/输出、评审、验证(V&V)、确认、设计转换、变更控制、DHF/DMR 索引，含 IEC 62366-1 人因工程挂点。适用于 II/III 类器械与 SaMD 的设计阶段质量体系搭建。

## 运行
```bash
python scripts/design_controls.py --demo
python scripts/design_controls.py --help
```

## 扩展契约（lgd-skeleton/1.0）
- **一切即插件**：仅依赖声明式 `module.json`，零配置。
- **按需装（lazy）**：仅 triggers 命中时加载。
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由。
- **扩展点**：`plugins/`(新增控制项：在 DESIGN_CATALOG 加一项，清单自动扩。)

## 红线
纯技术贡献，不含商业营销；MedXpert 仅作为贡献者署名（@stevenzhao07）。
