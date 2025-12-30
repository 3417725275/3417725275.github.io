# 3417725275.github.io（Hexo 博客仓库）

这是一个使用 **Hexo 7.3.0** 生成的静态博客项目，当前站点主题为 **Butterfly**。仓库中同时包含：

- **站点源码与配置**（用于写文章、改主题配置）
- **已生成的静态站点文件**（用于 GitHub Pages 直接访问）

## 目录说明（根目录）

> 提示：Hexo 的“生成目录”在根 `_config.yml` 中配置为 `public_dir: public`。本仓库为了 GitHub Pages 的访问习惯，也保留了**生成后的静态文件在根目录**（如 `index.html`、`archives/`、`css/` 等）的形式。

### 源码/配置相关（建议主要在这些目录里工作）

- **`source/`**：站点“源文件”目录（Hexo 的 `source_dir`）。
  - 通常包含文章（`source/_posts/`）、页面、以及文章资源（当 `post_asset_folder: true` 时每篇文章可有同名资源文件夹）。
  - 放在这里的静态资源可直接被拷贝/渲染到最终站点中。
- **`themes/`**：主题目录。
  - **`themes/butterfly/`**：Butterfly 主题源码（布局 `layout/*.pug`、样式 `source/css/*.styl`、脚本 `source/js/*` 等）以及主题配置文件 `themes/butterfly/_config.yml`。
- **`.cursor/`**：Cursor 编辑器相关的项目规则与说明文件（不影响站点构建，仅用于协作/规范）。

### 生成产物/线上可访问静态资源（通常由 `hexo generate` 生成）

这些目录/文件通

常是“构建后结果”，用于静态托管直接访问：

- **`index.html`**：站点首页的入口 HTML。
- **`archives/`**：归档页等相关页面的输出目录（由 Hexo 归档生成器生成，受根 `_config.yml` 的 `archive_dir` 影响）。
- **`2025/`**：按日期或永久链接规则生成的文章页面输出目录之一（示例：`2025/11/03/hello-world/index.html`）。
  - 具体路径由永久链接（根 `_config.yml` 的 `permalink` / `pretty_urls` 等）以及主题/插件共同决定。
- **`css/`**：站点前端 CSS 输出目录（如 `css/main.css`）。
- **`js/`**：站点前端 JavaScript 输出目录（主题脚本、搜索脚本等）。
- **`lib/`**：前端依赖库的静态文件（如 `font-awesome`、动画库等），供页面直接引用。
- **`images/`**：站点前端用到的图片资源输出目录（logo、favicon、图标等）。
- **`db.json`**：搜索索引数据文件（常见于 `hexo-generator-searchdb` 生成的本地搜索数据库）。

## 关键文件说明（根目录）

- **`_config.yml`**：Hexo 站点全局配置（站点信息、URL/permalink、目录配置、部署配置等）。
- **`package.json` / `package-lock.json`**：Node 依赖与脚本定义（用于安装 Hexo/插件并执行构建命令）。
- **`.gitignore`**：Git 忽略规则（通常会忽略 `node_modules/`、缓存、构建目录等）。

## 常用命令（Windows / npm）

在仓库根目录执行：

- **本地预览**：`npm run server`
- **生成静态文件**：`npm run build`
- **清理缓存/生成目录**：`npm run clean`
- **部署**：`npm run deploy`

## 维护建议

- 日常写作/改配置：优先修改 **`source/`**、根 **`_config.yml`**、主题配置 **`themes/butterfly/_config.yml`**。
- 如果需要深度改主题布局/样式，再进入 **`themes/butterfly/`** 修改主题源码。

