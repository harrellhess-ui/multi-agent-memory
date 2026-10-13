# 样本 · Claude 全局适配器

> **脱敏样本。** 原文件是本机真实在用的 Claude 全局入口兼专属适配器（100 行）。此处替换身份、路径、模型后端与插件清单，保留**职责划分、启动自检结构、项目适配器模板**这三样真正属于机制的东西。
> 尤其值得对照的是末尾的「项目 CLAUDE.md 模板」——**全局适配器里内嵌项目适配器模板**，这是让 Agent 自己能建项目适配器的关键。

---

# AB · Claude 全局适配器

本文件由 Claude Code 内核自动注入，是 Claude 原生全局入口与专属适配器。
共享身份、铁律、项目树和跨 Agent 规则以 `C:\Users\Demo\.agents\AB.md` 为唯一真相源。
说"收工""收尾""撤了""下了""结束""散会"，或说"同步一下""整理记忆""整理文档"时，
按 `AB.md`「收尾流程」执行，**其中详细步骤读取 `C:\Users\Demo\.agents\收尾流程.md`**，
不另立流程。

## 启动自检

内核注入本文件后，立即执行：

1. 称呼"AB"。
2. 确认当前工作目录和项目根目录。
3. 读取 `C:\Users\Demo\.agents\AB.md`。
4. 检查当前项目 `PROJECT_CONTEXT.md`：存在则读取；缺失则按 AB.md「新建项目规范」创建。
5. 检查当前项目 `CLAUDE.md`：存在则读取；缺失则按本文件「新建项目 CLAUDE.md 模板」创建。
6. 只在维护 Codex / DSH 制度、处理跨 Agent 冲突或修改 `CODEX.md` / `DSH.md` 时读取项目
   `CODEX.md` / `DSH.md`。
7. 审计加载链时，在文件读取和冲突检查完成后输出一次回执。
8. 若发现加载链异常（本文件未生效、目标文件缺失、`.agents` Git 追踪数不符或出现
   ReparsePoint），先报告并停止修改全局制度，待修复后再改。

## 专属规则

### Claude Auto Memory

- Auto Memory 保持启用，但不能代替明确读取 `PROJECT_CONTEXT.md`。
- 当前 Claude 内部索引、metadata、类型和链接格式属于版本实现细节，不是跨 Agent
  协议。
- 不保存项目当前状态、下一步、测试结果或正式文档中已经存在的技术事实。
- 与 `AB.md` 或 `PROJECT_CONTEXT.md` 冲突时立即失效。

### 多模态输入自动调用

<如果本端支持图像输入，写清是否原生读取、有无外挂依赖。不支持就删掉这节。>

## 新建项目 CLAUDE.md 模板

Claude 进入长期项目时，必须读取共享的 `PROJECT_CONTEXT.md`；项目根缺少 `CLAUDE.md`
时，由 Claude 按下列模板创建并只维护 Claude 专属规则。Claude 不代建、不要求
`CODEX.md` 或 `DSH.md`，其他 Agent 的项目适配器由各自全局适配器负责。

```markdown
# <项目名称> · Claude 项目适配器

## 启动自检

全局 CLAUDE.md 已自动加载。
全局真相源 `C:\Users\Demo\.agents\AB.md` 已读取。
开始项目任务前读取同目录 `PROJECT_CONTEXT.md`。

本项目工作目录：`<绝对路径>`
所属项目：<全局项目树中的项目名>

## Claude 专属规则

- <规则1>

## 变更记录

- YYYY-MM-DD：<日期与一句摘要>
```

## 部署环境

### Claude Code 配置

- 配置文件：`C:\Users\Demo\.claude\settings.json`；实际后端和模型以其中环境变量为准，
  回答版本或模型问题前重新读取，不凭本文件推断。
- 本地覆盖：`C:\Users\Demo\.claude\settings.local.json`
- <其他与你机制相关的开关，例如是否禁用自动压缩。没有就删。>

### 插件

<本端装了哪些插件。与机制无关，可整节删掉。>
