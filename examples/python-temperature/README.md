# Python 示例工作区：温度转换

这是一个小程序的参考成品。可以先运行，再对照项目上下文与适配器，了解每类信息如何落盘。

## 文件分工

```text
python-temperature/
├── temperature.py         程序入口与转换函数
├── test_temperature.py    单元测试及 CLI 测试
├── PROJECT_CONTEXT.md     项目目标、当前状态、决策和下一步
├── CLAUDE.md              Claude 项目适配器
├── CODEX.md               Codex 项目适配器
├── DSH.md                 DSH 项目适配器
├── .gitignore             Python 缓存与虚拟环境忽略规则
└── README.md              示例使用说明
```

三个适配器供对照。复制后只保留实际使用的端即可；项目共享事实都写在 [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)。

## 先运行

在这个目录打开终端，需要 Python 3.10 或更高版本：

```sh
python -B temperature.py 25
python -B -m unittest -v
```

第一条输出 `25.00 C = 77.00 F`。解释器名为 `python3` 时替换命令前缀。
更多检查项和实际运行记录见项目上下文“验证方式”。

## 复制成自己的项目

1. 将整个 `python-temperature` 目录复制到选定的位置，避免在公开仓库原件里练习。
2. 在新目录启动 Agent，让它确认工作目录与项目根目录。
3. 已配置本机制全局层时，沿用个人全局入口与收尾流程；未配置时先按[部署文档](https://github.com/harrellhess-ui/multi-agent-memory/blob/main/记忆机制与部署.md)接入，或仅用下面的显式读取方式体验项目层。
4. 按项目实际目标修改上下文。样例中的“已完成”仅描述附带代码，个人改动需重新验证。

本例提供项目文件，不会安装或修改全局配置。自动加载仍按各端接入方式设置；直接要求 Agent 读文件只能证明该次手动读取。

## 第一个 Agent：增加功能

把下面的任务交给当前端，适配器文件名按实际 Agent 选择：

```text
请先确认当前目录是复制出来的温度转换示例项目。
读取 PROJECT_CONTEXT.md 和本端的项目适配器（CLAUDE.md、CODEX.md 或 DSH.md）。
按上下文的“下一步”增加华氏转摄氏功能，先写测试，保持原命令兼容。
运行测试后更新 PROJECT_CONTEXT.md 的当前状态、验证记录和下一步，
保留“另一个 Agent 尚未复核”这项待办。不要把项目进度写进适配器。
```

收尾时使用个人全局入口中登记的流程文件。尚未配置该文件时，先取得公开仓库的 [收尾流程.md](https://github.com/harrellhess-ui/multi-agent-memory/blob/main/收尾流程.md)，确认其本地路径，再要求 Agent 显式读取。

## 第二个 Agent：读取并复核

新开另一个 Agent 的会话，不复制第一个 Agent 的聊天记录：

```text
请确认当前项目目录，读取 PROJECT_CONTEXT.md 和本端项目适配器。
说明程序已经支持什么、上次记录的测试结果是什么、还有什么未完成，并给出文件依据。
检查实现并重新运行测试，记录本次真实输出；完成后更新共享上下文，保留仍未解决的问题。
```

观察第二个 Agent 是否从文件恢复了项目状态，是否执行了验证，以及是否把结果写回共享上下文。它应区分上次记录与本次运行；无需在自己的适配器里复制一份进度。

## 对照一次收尾

| 本轮变化 | 更新位置 |
|---|---|
| 新增反向转换 | `temperature.py` 与 `test_temperature.py` |
| 功能完成、测试结果、复核待办 | `PROJECT_CONTEXT.md` |
| 新发现的某端独有操作要求 | 对应适配器；没有就不改 |
| 跨项目长期规则 | 经使用者确认后归个人全局真相源 |

程序测试通过只证明这份代码在记录的环境中运行；两端交接是否成功，需按实际会话另行记录。
