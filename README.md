# AI 代码视频提示词

用一段提示词，让 AI 写代码做视频。画面全部由 HTML + GSAP 画出来，再用 [HyperFrames](https://github.com/heygen-com/hyperframes) 逐帧渲染成 MP4，字不会糊，改一句台词只需改一行再渲染。

本仓库有两条片子和一段可直接复制的提示词：

| 目录 | 内容 |
| --- | --- |
| `prompts/editor-replica.md` | 提示词：手绘剪辑器里的小方块，30 秒 1:1 复刻版 |
| `replica/` | 复刻片工程，成片在 `replica/renders/editor-replica.mp4` |
| `workbuddy-tutorial/` | 45 秒教程片工程：在 WorkBuddy 里五步用这段提示词（成片含 WorkBuddy 吉祥物，只在公众号文章里发布） |

## 怎么用提示词

1. 打开 `prompts/editor-replica.md`，复制 `---` 下面的全部内容。
2. 把带 `【】` 的地方换成你自己的文件名和台词。
3. 发给能跑命令的 AI 编程助手，例如 Claude Code、Codex 或 WorkBuddy。
4. 等它装好 hyperframes、写代码、渲染，最后在工作目录里拿到 `.mp4`。

提示词第一句会让 AI 先装技能：

```bash
npx skills add heygen-com/hyperframes
```

需要 Node.js、ffmpeg，渲染时要联网（GSAP 从 CDN 加载）。AI 一般会自己检查环境，装不上会告诉你卡在哪。

## 在 WorkBuddy 里五步

1. 打开 WorkBuddy，点左上角「新建任务」。
2. 点输入框下方「选择工作空间」→「新建工作空间」，建一个空文件夹。
3. 先把提示词里 `【】` 的内容改成你的，再复制粘进输入框。提示词很长，WorkBuddy 会把它折叠成一个小卡片，这是正常的。
4. 点右下角发送，剩下交给它：装工具、写代码、渲染。
5. 看到「已完成」，去第 2 步的文件夹里打开 `.mp4`。

教程片里的界面截图来自 WorkBuddy V5.9.3。

## 自己渲染

```bash
cd replica
npm run check    # 布局和时间线检查
npm run render   # 输出到 renders/
```

`workbuddy-tutorial/` 用了 WorkBuddy 的官方吉祥物。界面截图已遮挡个人信息并放进仓库，单独的吉祥物图片版权属于腾讯，没有公开。想重渲教程片，先渲好 `replica/`，再把下面 4 个文件放到 `workbuddy-tutorial/assets/wb/`：

| 文件 | 用途 | 规格 |
| --- | --- | --- |
| `workbuddy-icon.png` | 窗口标题栏和对话头像 | 方形，约 66×66 |
| `mascot-peek.png` | 第 2 步从底部探头 | 透明底，约 200×128 |
| `mascot-laptop.png` | 主持人（抱笔记本） | 透明底，约 1080×1038 |
| `mascot-success-sprite.png` | 片尾庆祝动画 | 18 帧方形画面竖排成一张图，约 382×6876 |

然后运行 `bash workbuddy-tutorial/scripts/rerender.sh`（需要 ffmpeg）。`scripts/subset-font.py` 和 `scripts/mask-shots.py` 是维护用的：改字幕后重建字体子集、遮挡原始截图，需要 Python 和 [uv](https://github.com/astral-sh/uv)。

## 素材与版权

- 复刻片是对网上一条 30 秒剪辑短片的学习复刻：橙色方块角色、分镜和片尾署名都照搬原片，仅作学习交流，与原片作者及相关公司无关。原片版权归原作者。
- 仓库里的代码和提示词用 [MIT 许可](LICENSE)；字体、WorkBuddy 截图和复刻片照搬的角色设计不在此列。
- WorkBuddy 名称、界面和吉祥物属于腾讯。截图里的个人信息已遮挡。
- 字体：Caveat Brush、Patrick Hand、Noto Sans SC 使用 SIL OFL 1.1，Luckiest Guy 使用 Apache 2.0，许可证文件放在各自的 `assets/fonts/` 里。
