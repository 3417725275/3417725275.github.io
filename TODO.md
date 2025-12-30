# TODO：新主页（路线 A / 模板开发）MVP

## 概要（我们要做什么）

- **目标**：把站点根路径 `/` 改造成一个“最简主页（Landing Page）”，主页上有 **N 个模块卡片**（数量与内容来自配置文件），点击卡片跳转到对应页面。
- **约束/偏好**：
  - 走 **路线 A：学习前端模板开发**（在 Butterfly 主题中新增/修改 `pug` 模板完成主页结构）。
  - **主页不保留导航栏与页脚**（尽量简洁、专注卡片入口）。
  - 其中 **至少 1 个卡片**点击后跳转到“原来的博客首页（文章列表）”。
- **关键改造**：把“原文章列表首页”从 `/` 挪到 **`/blog/`**，让 `/` 空出来做新主页。

## 实现方案（核心关系）

- **Hexo**：负责把 `source/` + 配置渲染成静态站点。
- **Butterfly**：负责页面模板与主题资源（Pug/CSS/JS）。我们将：
  - 新增一个主页布局模板：`themes/butterfly/layout/home.pug`
  - 用 `source/index.md` 指定 `layout: home` 来生成 `/`
  - 在 `themes/butterfly/_config.yml` 配置卡片列表（N 个）

## 任务清单（按顺序做）

### 1）迁移原“文章列表首页”到 `/blog/`

- [ ] 修改根 `_config.yml`：将 `index_generator.path` 从 `''` 改为 `blog`
- [ ] 更新主题菜单（`themes/butterfly/_config.yml` 的 `menu`）：
  - [ ] “博客/文章”指向 `/blog/`（作为原首页入口）

**验收**：
- [ ] 访问 `/blog/` 能看到原来的文章列表首页（含分页）
- [ ] `/` 不再被文章列表占用

### 2）增加主页卡片配置（数据驱动 N 张卡片）

- [ ] 在 `themes/butterfly/_config.yml` 新增主页配置段，例如：
  - `home_page.enable`
  - `home_page.title / subtitle`
  - `home_page.cards[]`（每项包含 `title/desc/icon/link` 等）
- [ ] 配置一张卡片（例如“计算几何”）的 `link` 指向 **`/blog/`**（用于跳回原博客首页）

**验收**：
- [ ] 仅改配置即可增/删卡片数量（无需改模板）

### 3）新增主页模板（路线 A：Pug）

- [ ] 新增 `themes/butterfly/layout/home.pug`：
  - [ ] 复用主题 `includes/head.pug`（保证基础 CSS/字体/配置注入可用）
  - [ ] **不引入**：导航栏、页脚、侧边栏、右下角按钮等（保持“最简”）
  - [ ] 根据 `theme.home_page.cards` 循环渲染卡片 HTML

**验收**：
- [ ] 打开 `/` 能渲染出主页内容
- [ ] 卡片数量与配置一致
- [ ] 点击卡片按配置正确跳转

### 4）创建 `/` 的入口页面

- [ ] 新增 `source/index.md`（或其他 source 页面文件）：
  - [ ] front-matter 指定 `layout: home`
  - [ ] 建议加 `type: home`（生成 `.type-home` 作用域，便于只给主页写 CSS）
  - [ ] 建议加 `comments: false`、`aside: false`

**验收**：
- [ ] `/` 使用 `home.pug` 布局而不是默认 `page.pug`

### 5）主页样式（可先复用现有 custom.css）

- [ ] 在 `source/css/custom.css` 增加主页样式（建议以 `.type-home` 为作用域前缀）：
  - [ ] 卡片网格布局（响应式）
  - [ ] hover 交互（轻微上浮、阴影、边框高亮）
  - [ ] 字体层级与间距（让页面“高级感”更强）

**验收**：
- [ ] 主页样式只影响 `/`，不影响文章页/归档页

### 6）本地构建与验证

- [ ] `npm run clean`
- [ ] `npm run build`
- [ ] `npm run server`
- [ ] 验证：
  - [ ] `/`：最简主页（无 nav/footer），卡片正常显示
  - [ ] 点击“计算几何”卡片 → `/blog/`（原文章列表首页）
  - [ ] `/blog/`：文章列表与分页正常

## 涉及文件一览（预计会改/新增）

- 修改：
  - `_config.yml`（index_generator.path）
  - `themes/butterfly/_config.yml`（新增 `home_page` 配置、更新菜单）
  - `source/css/custom.css`（主页样式）
- 新增：
  - `themes/butterfly/layout/home.pug`（主页模板）
  - `source/index.md`（主页入口页面）

## 注意事项（影响面）

- **URL/SEO**：原首页文章列表路径变为 `/blog/`，分页路径也会变化（例如 `/blog/page/2/`）。
- **主题升级风险**：路线 A 会改/加主题模板文件，后续升级 Butterfly 时需要关注差异（建议只新增文件、尽量少改主题核心文件）。

