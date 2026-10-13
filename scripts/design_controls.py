#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
design_controls.py — 设计控制清单生成器
========================================
按 ISO 13485:2016 §7.3（设计开发控制）与 21 CFR 820.30（设计控制）生成
自查清单，含 IEC 62366-1 人因工程挂点。按阶段过滤输出 Markdown。

法规版本说明（2026-10 核实）：FDA QMSR（21 CFR Part 820 修订版）已于
2026-02-02 生效，将 ISO 13485:2016 并入法规，取代原 820.30 等设计控制条款
（含 820.30(b)–(j) 分段表述）。本清单保留 820.30 条款号作为历史版本锚点，
出口企业须按 QMSR 现行文本与 ISO 13485:2016 条款重新对照。

阶段（ISO 13485 §7.3.2–7.3.10）：
  策划 / 输入 / 输出 / 评审 / 验证 V&V / 确认 Validation /
  设计转换 / 更改控制 + DHF/DMR 索引

诚实边界：清单按通用要求整理；具体产品须按目标辖区法规二次裁剪，
不构成法规建议。
"""
from __future__ import annotations
import argparse
import os
import sys

# (阶段, 条目, 依据)
DESIGN_CATALOG = [
    ("策划", "制定设计与开发计划，明确阶段/职责/接口/更新控制", "ISO 13485 §7.3.2 / 820.30(b)"),
    ("策划", "计划经评审与批准，按项目规模调整", "ISO 13485 §7.3.2"),
    ("输入", "设计输入完整：预期用途/功能/性能/安全/法规要求/风险", "ISO 13485 §7.3.3 / 820.30(c)"),
    ("输入", "设计输入经评审（含糊项解决）并批准", "§7.3.3"),
    ("输入", "输入与风险管理文件（ISO 14971）关联", "跨标准挂点"),
    ("输出", "设计输出满足输入，规定验收准则", "ISO 13485 §7.3.4 / 820.30(d)"),
    ("输出", "输出经批准后发布，标识关键安全特性", "§7.3.4"),
    ("评审", "按计划阶段执行系统评审（代表性专家参加）", "ISO 13485 §7.3.5 / 820.30(e)"),
    ("验证", "设计验证 V&V：输出满足输入（测试/分析/演示）", "ISO 13485 §7.3.6 / 820.30(f)"),
    ("确认", "设计确认 Validation：满足预期用途/用户需求", "ISO 13485 §7.3.7 / 820.30(g)"),
    ("人因", "可用性工程：use scenarios / use errors 纳入验证确认", "IEC 62366-1 §5.4-5.8（挂点）"),
    ("转换", "设计转换：设计输出→生产信息（DMR/BOM/工艺/检验）", "ISO 13485 §7.3.8"),
    ("更改", "设计更改：识别/评审/验证/确认/批准，影响评估", "ISO 13485 §7.3.9 / 820.30(i)"),
    ("更改", "更改对在制品/已交付产品/注册证的影响评估", "§7.3.9"),
    ("追溯", "DHF 索引：每条设计记录映射到生命周期阶段", "820.30(j)（DHF；820.185 为质量体系记录，非 DHF，历史勘误删除）"),
    ("追溯", "DMR 索引：生产与检验文件齐备", "820.181 / 820.184"),
]

STAGES = sorted({s for s, _, _ in DESIGN_CATALOG})


def checklist(stage: str | None = None) -> list[tuple[str, str, str]]:
    if not stage:
        return DESIGN_CATALOG
    return [row for row in DESIGN_CATALOG if row[0] == stage]


def render_md(rows: list[tuple[str, str, str]], title: str) -> str:
    lines = [f"# {title}", "",
             "> 由 design_controls.py 生成。依据：ISO 13485:2016 §7.3 / 21 CFR 820.30（历史版本；"
             "QMSR 2026-02-02 起以 ISO 13485:2016 为准，详见文件头说明） / IEC 62366-1。",
             "", "| # | 阶段 | 自查项 | 依据 | 状态 |", "|---|---|---|---|---|"]
    for i, (stage, item, src) in enumerate(rows, 1):
        lines.append(f"| {i} | {stage} | {item} | {src} | ☐ |")
    return "\n".join(lines)


def _demo() -> int:
    print("设计控制清单生成器 · 演示\n")
    print(f"阶段: {' / '.join(STAGES)}\n")
    for stage, item, src in DESIGN_CATALOG[:6]:
        print(f"  [☐] ({stage}) {item}")
        print(f"      依据: {src}")
    print(f"\n[demo] 共 {len(DESIGN_CATALOG)} 项；--stage 过滤，--out 落盘 Markdown。")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="设计控制清单生成器")
    ap.add_argument("--demo", action="store_true", help="跑内置演示")
    ap.add_argument("--stage", choices=STAGES, help="按阶段过滤")
    ap.add_argument("--out", help="输出 Markdown 路径（缺省打印）")
    args = ap.parse_args()

    if args.demo:
        return _demo()
    rows = checklist(args.stage)
    title = f"设计控制自查清单（{args.stage}）" if args.stage else "设计控制自查清单（全阶段）"
    md = render_md(rows, title)
    if args.out:
        # 自动创建父目录；失败给出友好错误而非裸 traceback（2026-10-12 压力测试修复）
        parent = os.path.dirname(os.path.abspath(args.out))
        try:
            os.makedirs(parent, exist_ok=True)
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(md + "\n")
        except OSError as e:
            print(f"[error] 无法写入 {args.out}: {e}", file=sys.stderr)
            return 2
        print(f"[ok] 已写 {args.out}（{len(rows)} 项）")
        return 0
    print(md)
    return 0


if __name__ == "__main__":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
