import os
import shutil

posts_dir = 'source/_posts'
src_dir = os.path.join(posts_dir, '曲线曲面')

# 定义要移动的文件和目标目录
files_to_move = [
    ('贝塞尔曲线.md', '计算几何/几何表示/曲线表示'),
    ('贝塞尔曲线', '计算几何/几何表示/曲线表示'),
    ('B样条曲线.md', '计算几何/几何表示/曲线表示'),
    ('B样条曲线', '计算几何/几何表示/曲线表示'),
    ('NURBS曲线.md', '计算几何/几何表示/曲线表示'),
    ('样条曲面.md', '计算几何/几何表示/曲面表示'),
    ('样条曲线曲面的插值拟合.md', '计算几何/几何算法/曲线曲面算法'),
]

# 创建目标目录
for _, dst in files_to_move:
    dst_path = os.path.join(posts_dir, dst)
    os.makedirs(dst_path, exist_ok=True)
    print(f'Created directory: {dst_path}')

# 移动文件
for filename, dst in files_to_move:
    src_path = os.path.join(src_dir, filename)
    dst_path = os.path.join(posts_dir, dst, filename)

    if os.path.exists(src_path):
        try:
            shutil.move(src_path, dst_path)
            print(f'Moved: {src_path} -> {dst_path}')
        except Exception as e:
            print(f'Error moving {src_path}: {e}')
    else:
        print(f'File not found: {src_path}')

print('Done!')
