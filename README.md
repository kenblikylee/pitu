# pitu
python 开源命令行P图工具。

## 安装

``` sh
pip install pitu
```

## 命令行使用方式

### 缩放 zoom

pitu zoom <photo_path> <ratio> [width [height]]

``` sh
pitu zoom photo.jpg 0.5
pitu zoom photo.jpg 0 600
pitu zoom photo.jpg 0 0 300
```

### 旋转 rotate

pitu rotate <photo_path> <angle> [color]

``` sh
pitu rotate photo.jpg 45
pitu rotate photo.jpg 45 green
pitu rotate photo.jpg 45 '#ff0000'
```

### 翻转(镜像) flip

pitu flip <photo_path> <x|y>

``` sh
pitu flip photo.jpg x
pitu flip photo.jpg y
```

### 裁剪 cut

pitu cut <photo_path> &lt;x&gt; &lt;y&gt; &lt;width&gt; &lt;height&gt;

``` sh
pitu cut photo.jpg 100 100 200 200
```

### 灰度 gray

pitu gray <photo_path>

``` sh
pitu gray photo.jpg
```

### 文本 text

pitu text <photo_path> &lt;text&gt; [x [y [font_size [color [pf|yh]]]]]

``` sh
pitu text photo.jpg '我的P图工具'
pitu text photo.jpg '我的P图工具' 300 100
pitu text photo.jpg '我的P图工具' 300 100 50
pitu text photo.jpg '我的P图工具' 300 100 50 '#f0f'
pitu text photo.jpg '我的P图工具' 300 100 50 blue pf
pitu text photo.jpg '我的P图工具' 300 100 50 cyan yh
```

### 拼图 pin

pitu pin <x|y> &lt;photo1_path photo2_path [photo3_path ... photon_path]&gt; [diff]

``` sh
pitu pin x zoom-photo.jpg rotate-photo.jpg flip-photo.jpg cut-photo.jpg gray-photo.jpg  text-photo.jpg
pitu pin y zoom-photo.jpg rotate-photo.jpg flip-photo.jpg cut-photo.jpg gray-photo.jpg  text-photo.jpg

pitu pin x zoom-photo.jpg rotate-photo.jpg flip-photo.jpg cut-photo.jpg gray-photo.jpg  text-photo.jpg diff
pitu pin y zoom-photo.jpg rotate-photo.jpg flip-photo.jpg cut-photo.jpg gray-photo.jpg  text-photo.jpg diff
```

### 头像 avatar

pitu avatar <photo_path> [mode]

``` sh
pitu avatar photo.jpg
pitu avatar photo.jpg ex
```

### 封面 cover

pitu cover <photo_path> [mode [ratio]]

``` sh
pitu cover photo.jpg
pitu cover photo.jpg ex
pitu cover photo.jpg ce '16:9'
pitu cover photo.jpg ex '16:9'
```

### 9宫格和任意网格 grid

pitu grid &lt;photo1_path photo2_path [photo3_path ... photon_path]&gt;  \ <br>
    [':rows=行数 :cols=列数 :width=宽 :height=高 :gap=间距 :padding=边距 :color=背景色']

``` sh
pitu grid 1.jpg 2.jpg 3.jpg 4.jpg 5.jpg 6.jpg 7.jpg 8.jpg 9.jpg

pitu grid 1.jpg 2.jpg 3.jpg 4.jpg ':rows=2 :cols=2 :width=600 :height=300 :gap=10 :padding=20 :color=#555'
```
