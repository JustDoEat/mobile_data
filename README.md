人脸测试的一些小脚本和教程。

===================================================================

[TOC]

# 参考资料

https://github.com/vinta/awesome-python

https://github.com/jobbole/awesome-python-cn

交流QQ群：python 测试开发 144081101

wechat： pythontesting

淘宝天猫可以把链接发给qq850766020，为你生成优惠券，降低你的购物成本！

快来领取支付宝跨年红包！1月1日起还有机会额外获得专享红包哦！复制此消息，打开最新版支付宝就能领取！2C56CV70sA

# 测试开发

## UI测试

 * appium - 移动端UI自动化测试。 [链接](https://github.com/appium/python-client) --推荐

 * selenium - web UI自动化测试。 [链接](https://github.com/SeleniumHQ/selenium/tree/master/py) --推荐

 * uiautomator- 安卓UI自动化测试。 [链接](https://github.com/xiaocong/uiautomator) --推荐

 * pyautoacad - AutoCAD自动化。 [链接](https://github.com/reclosedev/pyautocad) 

 * sikuli - 位图自动化。 [链接](http://www.sikuli.org) 

 * monkeyrunner- 安卓自动化。 [链接](https://developer.android.com/studio/test/monkeyrunner/index.html) 

 * pywinauto - Windows UI自动化。 [链接](https://github.com/pywinauto/pywinauto/) 

 * ldtp - Linux UI自动化。 [链接](https://pypi.python.org/pypi/ldtp) 

 * dogtail- Linux UI自动化。 [链接](https://pypi.python.org/pypi/dogtail) 

 * pyautogui- 跨平台的UI自动化工具，控制鼠标和键盘。 [链接](https://github.com/asweigart/pyautogui) 

 * pyautoit- autoit python api。 [链接](https://github.com/jacexh/pyautoit) 

 * splinter - web UI测试工具，基于selnium封装。 [链接](https://github.com/cobrateam/splinter) 

 * 雪峰磁针石说明:

autopy、WATSUP、winGuiAuto因为较长时间未更新未收录

## 性能测试


 * funkload - 性能及功能测试工具。 [链接](http://funkload.nuxeo.org/) --推荐

 * multi-mechanize - python性能测试工具，基于多进程和多线程，是学习性能测试goon工具的佳品。 [链接](https://github.com/cgoldberg/multi-mechanize) --推荐

 * locust - 强大的性能测试工具，使用了协程。 [链接](https://github.com/locustio/locustt) --推荐

 * ngrinder - 市面上最强大的性能测试工具之一，主要用jython书写脚本，性能在loadrunner和jmeter之上，扩展性好。 [链接](https://github.com/naver/ngrinder) --强烈推荐

 * boom - 类似ab(ApacheBench)的性能测试工具。 [链接](https://github.com/tarekziade/boom) 

## 测试框架


 * Hypothesis - 高级单元测试测试框架，支持行为驱动，基于property 。 [链接](https://github.com/HypothesisWorks/hypothesis-python) -- 推荐 

 * unittest - (Python 标准库) 单元测试框架 [链接](https://docs.python.org/2/library/unittest.html) -- 推荐 

 * mamba  - 行为驱动测试框架。 [链接](https://github.com/nestorsalceda/mamba) 

 * nose- 更好的单元测试框架。 [链接](https://github.com/nose-devs/nose) -- 推荐 

 * nose2- nose基于unittest2的版本。 [链接](https://github.com/nose-devs/nose2) 

 * pytest- 很好的强大的单元测试框架，实际上广泛使用在自动化单元、接口、功能等测试。 [链接](https://github.com/pytest-dev/pytest) -- 强烈推荐 


 * Robot Framework- 通用的python测试框架，易于上手，生成的报告比较好看，适合小型公司使用，支持关键字和数据等驱动，系业界内很出名的框架。不过因为写用例不能很灵活的应用python，需要大量的python封装，大公司通常使用pytest，django，flask之类的库自行开发。 [链接](https://github.com/robotframework/robotframework) 

 * pytest- 很好的强大的单元测试框架，实际上广泛使用在自动化单元、接口、功能等测试。 [链接](https://github.com/pytest-dev/pytest)  -- 强烈推荐 

 * green- 彩色(命令行能显示多种颜色)的单元测试框架。 [链接](https://github.com/CleanCut/green) 

 * tox- 基于virtualenv的测试框架，主要用于解决多版本python问题。 [链接](https://github.com/tox-dev/tox) 

 * sixpack- A/B 测试框架。 [链接](https://github.com/sixpack/sixpack) 

 * lettuce- 行为驱动 测试框架。 [链接](https://github.com/gabrielfalcao/lettuce) 

 * pyccuracy- 行为驱动 web验收测试框架。 [链接](https://github.com/heynemann/pyccuracy) 

 * pytest-bdd- 基于pytest的行为驱动 测试框架。 [链接](https://github.com/pytest-dev/pytest-bdd) 


## Mock

 * doublex：强大的测试桩框架。[链接](https://bitbucket.org/DavidVilla/python-doublex) 

 * mock：(Python3 标准库) mock和patch。[链接](https://docs.python.org/3/library/unittest.mock.html) 

 * freezegun：伪造时间。[链接]https://github.com/spulec/freezegun) 

 * httmock：Python 2.7+ 和 3.4+ mock requests库。[链接](https://github.com/patrys/httmock) 

 * httpretty：Python 的 HTTP 请求 客户端mock 工具，暂时不支持python3。[链接](https://github.com/tox-dev/tox) 

 * responses：针对requests 库的mock库。[链接](https://github.com/getsentry/responses) 

 * VCR.py：录制HTTP请求加快测试执行速度并可进行mock。[链接](https://github.com/kevin1024/vcrpy) -- 推荐 

 * factoryboy：Python测试fixtures(setup和teardown)替代库。[链接](https://github.com/FactoryBoy/factory_boy) 

 * mixer：另外一个测试fixtures(setup和teardown)替代库，支持 Django, Flask, SQLAlchemy, Peewee 等。[链接](https://github.com/klen/mixer) 

 * modelmommy：为 Django测试创建随机fixtures [链接](https://github.com/vandersonmota/model_mommy) 

 * faker：生成多种伪数据。[链接](https://github.com/joke2k/faker) 

 * fake2db：伪造数据库生成器。[链接](https://github.com/emirozer/fake2db) 

 * mimesis：生成mock数据。[链接]https://github.com/lk-geimfari/mimesis) 

 * 雪峰磁针石说明:

radar 因为github星级太少而未收录

## 其他测试工具

 * coverage：代码覆盖率。[链接](https://bitbucket.org/ned/coveragepy) 

 * FuckIt.py：代码出错也可以执行。[链接](https://github.com/ajalt/fuckitpy) 

  * RoboBrowser：一个简单的，Python 风格的库，用来浏览网站，而不需要一个独立安装的浏览器。[链接](https://github.com/jmcarp/robobrowser) 

  * MechanicalSoup：用于自动和网络站点交互的 Python 库。[链接](https://github.com/MechanicalSoup/MechanicalSoup) 

  * augmented-traffic-control：网络模拟工具。[链接](https://github.com/facebook/augmented-traffic-control) -- 强烈推荐 



## 持续交付

 * buildbot - google等公司使用的持续集成框架，上手比Jenkins难，功能和性能远比Jenkins强大。 [链接](https://github.com/buildbot/buildbot/)

 * BitBake – 嵌入式Linux上类似make工具。[链接](http://www.yoctoproject.org/docs/1.6/bitbake-user-manual/bitbake-user-manual.html)

 * buildout – 用于从多个部分创建，组装和部署应用程序的构建系统。[链接](hhttps://github.com/buildout/buildout/blob/master/doc/index.rst)

 * PlatformIO – 在不同的开发平台的控制台构建工具。[链接](https://github.com/platformio/platformio-core)

 * PyBuilder – 纯Python编写的持续构建工具。[链接](https://github.com/buildbot/buildbot/)

 * SCons – 软件构建工具。[链接](https://github.com/SCons/scons)

## 测试工具对接

 * jira –自动化JIRA。[链接](https://github.com/pycontribs/jira)

# awesome-python

## 管理面板

用于管理界面的库。

 * Ajenti - Linux & BSD web管理面板。管理进程和文件等。 [链接](https://github.com/ajenti/ajenti) 

 * django-suit - 现代主题的Django管理界面（仅限非商业用途）。[链接](https://github.com/darklow/django-suit) 

 * django-xadmin -  方便的Django admin替代。 完全支持插件扩展，基于 Twitter Bootstrap，并有站内书签、支持 xls, csv, xml和json数据导入等不少增强。 [链接](https://github.com/sshwsfc/xadmin) 


 * flask-admin - Flask的简单和可扩展的 web 管理界面框架。  [链接](https://github.com/flask-admin/flask-admin) 

 * flower  - Celery的实时监控和网络。 [链接](https://github.com/flask-admin/flask-admin) 

 * Grappelli - Django管理界面的爵士皮肤。[链接]https://github.com/sehmaschine/django-grappelli) 

 * Wooey - 为Python脚本创建自动Web UI的Django应用程序。 [链接](https://github.com/wooey/wooey) 

## 算法和设计模式

Python的算法和设计模式的实现。

 * algorithms - Python的算法模块。 [链接](https://github.com/nryoung/algorithms) 
 
 * PyPattyrn - 简单有效实现通用设计模式。 [链接](https://github.com/tylerlaberge/PyPattyrn) 

 * python-patterns - Python中设计模式的集合。 [链接](https://github.com/faif/python-patterns) 

 * sortedcontainers - SortedList，SortedDict和SortedSet类型的快速，纯Python实现。 [链接](https://github.com/grantjenks/sorted_containers/) 



## 反病毒

 * django-simple-captcha - 简单且高度可定制的Django应用，可以将验证码图像添加到任何Django表单。 [链接](https://github.com/mbi/django-simple-captcha) 

 * 雪峰磁针石说明:

django-simple-spam-blocker因为github星级太少而未收录


## 资产管理

用于管理，压缩和缩小网站资产的工具。

 * django-compressor - 将链接和内联的JavaScript或CSS压缩到单个缓存文件中。 [链接](https://github.com/django-compressor/django-compressor) 

 * django-pipeline - Django的资产包装库。 [链接](https://github.com/jazzband/django-pipeline) 

 * django-storages - Django自定义存储后端集。 [链接](https://github.com/jschneier/django-storages) 

 * fanstatic - 用 Python 的包的方式封装，优化静态文件并解依赖。 [链接](http://www.fanstatic.org/en/latest/intro.html) 

 * fileconveyor - 检测和同步文件到CDN，S3和FTP的后台程序。 [链接](https://github.com/wimleers/fileconveyor) 

 * flask-assets - 集成web 资源到Flask应用。 [链接](https://github.com/faif/python-patterns) 

 * jinja-assets-compressor - Jinja扩展程序，用于编译和压缩资源。 [链接](https://github.com/faif/python-patterns)  -- github星级不到100.

 * webassets - 为静态资源打包，优化和管理基于缓存的唯一URL。 [链接](https://github.com/miracle2k/webassets) 



## 音频

操作音频的库。

 * audiolazy -  数字信号处理（DSP）软件包。 [链接](https://github.com/danilobellini/audiolazy) 

 * audioread - 跨库（GStreamer +Core Audio+ MAD + FFmpeg）音频解码。[链接](https://github.com/beetbox/audioread) 

 * beets - 音乐库管理和MusicBrainzb标签。[链接](https://github.com/beetbox/beets)  -- 推荐

 * dejavu - 音频指纹识别。[链接](https://github.com/worldveil/dejavu) -- 推荐

 * id3reader - 用于读取MP3元数据的Python模块。[链接](https://nedbatchelder.com/code/modules/id3reader.py) 

 * m3u8 - 解析m3u8文件的模块。[链接](https://github.com/globocom/m3u8) 

 * mingus - 先进的音乐理论和MIDI文件和播放支持符号包。[链接](https://github.com/bspaans/python-mingus) 

 * mutagen - 用于处理音频元数据的Python模块。[链接](https://github.com/quodlibet/mutagen) 

 * pyAudioAnalysis - Python音频分析库：特征提取，分类，分割和应用。[链接](https://github.com/tyiannak/pyAudioAnalysis)  -- 推荐

 * pydub - 通过简单易用的高级界面处理音频。[链接](https://github.com/jiaaro/pydub) -- 推荐

 * pyechonest - Echo Nest API的Python客户端。[链接](https://github.com/echonest/pyechonest) 

 * talkbox - 用于语音/信号处理的Python库。[链接](https://github.com/miracle2k/webassets) 

 * TimeSide - 开放的Web音频处理框架。[链接](https://github.com/Parisson/TimeSide) 

 * tinytag - 用于读取MP3，OGG，FLAC和Wave文件的音乐元数据的库。[链接](https://github.com/devsnd/tinytag) 

 * 雪峰磁针石说明:

django-elastic-transcoder， eyeD3 因为github星级太少而未收录

scikits.talkbox 因长时间未更新未收录

## 认证

 * Authomatic：简单但是强大的框架，身份验证/授权客户端。[链接](https://github.com/authomatic/authomatic) 

 * django-allauth：Django 的验证应用。[链接](https://github.com/pennersr/django-allauth) 

 * django-oauth-toolkit： Django OAuth2。[链接](https://github.com/evonove/django-oauth-toolkit) 

 * django-oauth2-provider：Django OAuth2。[链接](https://github.com/caffeinehit/django-oauth2-provider) 

 * Flask-OAuthlib： Flask OAuthlib 。[链接](https://github.com/lepture/flask-oauthlib) 

 * OAuthLib： 通用完整的实现OAuth请求-签名逻辑。[链接](https://github.com/idan/oauthlib) 

 * python-oauth2：创建 OAuth 客户端和服务端完全测试的抽象接口。[链接](https://github.com/joestump/python-oauth2) 

 * python-social-auth：设置简单的社交认证。[链接](https://github.com/python-social-auth/social-core) 

 * rauth：OAuth 1.0/a, 2.0, 和 Ofly。[链接](https://github.com/litl/rauth) 

 * sanction：一个超级简单的OAuth2 客户端实现。[链接](https://github.com/demianbrecht/sanction) 

 * PyJWT：JSON Web 令牌草案 01。[链接](https://github.com/jpadilla/pyjwt) 

 * python-jwt：生成和验证 JSON Web 令牌。[链接](https://github.com/davedoesdev/python-jwt) 


 * 雪峰磁针石说明:

jose，python-jws因为github星级太少而未收录

scikits.talkbox 因长时间未更新未收录

## CMS

内容管理系统

 * django-cms：开源的，基于Django的企业级 CMS。[链接](https://www.django-cms.org/en/) 

 * djedi-cms：轻量级但却非常强大的 Django CMS ，考虑到了插件，内联编辑以及性能。[链接]http://djedi-cms.org/) 

 * FeinCMS：基于 Django 构建的最先进的内容管理系统之一。[链接](https://github.com/feincms/feincms/) 

 * Kotti：高层的的web应用框架，基于 Pyramid 构建。[链接](https://github.com/Kotti/Kotti) 

 * Mezzanine：强大的，一致的，灵活的内容管理平台。[链接](https://github.com/stephenmcd/mezzanine)  -- 推荐

 * Opps：杂志，报纸网站以及大流量门户网站设计的 CMS 平台，基于 Django。[链接]https://github.com/opps/opps) 

 * Plone：构建于开源应用服务器 Zope 之上的 CMS。[链接](https://plone.org/) 

 * Quokka：灵活，可扩展的小型 CMS，基于 Flask 和 MongoDB。[链接](https://github.com/quokkaproject/quokka)
 
 * Wagtail：Django 内容管理系统。[链接](https://github.com/wagtail/wagtail) -- 推荐

 * Widgy： CMS 框架，基于 Django。[链接](https://wid.gy/) 



## 缓存

缓存数据的库。

 * Beaker：缓存和会话库，可以用在 web 应用和独立 Python脚本和应用上。[链接](https://github.com/bbangert/beaker) 

 * DiskCache：Python磁盘缓存（Django兼容）。。[链接](https://github.com/grantjenks/python-diskcache/) 

 * django-cache-machine：Django 模型的自动缓存和失效。[链接](https://github.com/django-cache-machine/django-cache-machine) 

 * django-cacheops：具有自动颗粒化事件驱动失效功能的 ORM。[链接](https://github.com/Suor/django-cacheops) 

 * dogpile.cache：dogpile.cache 是 Beaker 的替代，由同一作者开发。[链接](http://dogpilecache.readthedocs.io/en/latest/) 

 * HermesCache：Python 缓存库，具有基于标签的失效和 dogpile effect 保护功能。[链接](https://bitbucket.org/saaj/hermes/) 

 * johnny-cache：django应用缓存框架。[链接]https://github.com/jmoiron/johnny-cache) 

 * pylibmc：libmemcached 接口的 Python 封装。[链接](https://github.com/lericson/pylibmc) 

 * 雪峰磁针石说明:

django-viewlet因为github星级太少而未收录

## 自动聊天工具

 * Errbot：最简单和最流行的聊天机器人用来实现自动聊天工具。[链接](https://github.com/errbotio/errbot/) 


## 代码分析和lint

 * coala：语言独立和易于扩展的代码分析应用程序。[链接](https://pypi.python.org/pypi/coala/0.12.0.dev20171216122902) 

 * code2flow：把你的 Python 和 JavaScript 代码转换为流程图。暂时无法继续维护。[链接](https://github.com/scottrogowski/code2flow) 

 * pycallgraph：这个库可以把你的Python 应用的流程(调用图)进行可视化。[链接](https://github.com/gak/pycallgraph) 

 * Flake8：模块化源码检查工具: pep8, pyflakes 以及 co。[链接](https://gitlab.com/pycqa/flake8) 

 * Pylint：一个完全可定制的源码分析器。[链接](https://github.com/PyCQA/pylint) 

 * pylama：python代码审计。[链接](https://github.com/klen/pylama) 

 * YAPF: Google的Python代码格式化工具。[链接](https://github.com/google/yapf) --推荐

 * pylama：Python 和 JavaScript 的代码审查工具。[链接](https://github.com/klen/pylama/blob/develop/docs/index.rst) 

 * autopep8：自动格式化 Python 代码，以使其符合 PEP8 规范。[链接](https://github.com/hhatto/autopep8) --推荐

 * mypy ：静态类型检查。[链接](https://github.com/python/mypy) --推荐

 * pep8 ：python风格检查。[链接](https://github.com/PyCQA/pycodestyle) --推荐

## 命令行工具。

### 命令行程序开发

 * asciimatics：跨平台，全屏终端包（即鼠标/键盘输入和彩色，定位文本输出），完整的复杂动画和特殊效果的高级API。[链接](https://github.com/peterbrittain/asciimatics) 

 * cement：Python 的命令行程序框架。[链接](https://github.com/datafolklabs/cement/) 

 * click：一个通过组合的方式来创建精美命令行界面的包。[链接](https://github.com/pallets/click) --推荐

 * cliff：一个用于创建命令行程序的框架，可以创建具有多层命令的命令行程序。[链接](https://git.openstack.org/cgit/openstack/cliff) 

 * clint：Python 命令行程序工具。[链接](https://github.com/kennethreitz/clint) 

 * colorama：跨平台彩色终端文本。[链接](https://github.com/tartley/colorama) 

 * docopt：Python 风格的命令行参数解析器。[链接](https://github.com/docopt/docopt) --推荐

 * Gooey：一条命令，将命令行程序变成一个 GUI 程序。[链接](https://github.com/chriskiehl/Gooey) 

 * Python-Fire：将命令行程序变成一个 GUI 程序。[链接](https://github.com/google/python-fire) --推荐

 * python-prompt-toolkit：构建强大的交互式命令行程序的库。[链接](https://github.com/jonathanslenders/python-prompt-toolkit) --推荐

 * Pythonpy：在命令行中直接执行任何Python指令。[链接](https://github.com/Russell91/pythonpy) 

### 生产力工具

 * aws-cli：Amazon Web Services 的通用命令行界面。[链接](https://github.com/aws/aws-cli) 

 * bashplotlib：在终端中进行基本绘图。[链接](https://github.com/glamp/bashplotlib) 

 * caniusepython3：判断是哪个项目妨碍你你移植到 Python 3。[链接](https://github.com/brettcannon/caniusepython3) 

 * cookiecutter：从 cookiecutters（项目模板）创建项目的一个命令行工具。[链接](https://github.com/brettcannon/caniusepython3) 

 * doitlive：一个用来在终端中进行现场演示的工具。[链接](https://github.com/sloria/doitlive) 

 * howdoi：通过命令行获取即时的编程问题解答。[链接](https://github.com/gleitz/howdoi) --推荐

 * httpie：命令行HTTP 客户端，cURL 的替代品，易用性更好。[链接](https://github.com/jakubroztocil/httpie) 

 * PathPicker：从bash输出中选出文件。[链接](https://github.com/facebook/PathPicker) 

 * percol：向UNIX shell 传统管道概念中加入交互式选择功能。[链接](https://github.com/mooz/percol) 

 * SAWS：一个加强版的 AWS 命令行。[链接](https://github.com/donnemartin/saws) 

 * thefuck：修正你之前的命令行指令。[链接](https://github.com/nvbn/thefuck) 

 * mycli：一个 MySQL 命令行客户端，具有自动补全和语法高亮功能。[链接](https://github.com/dbcli/mycli) --推荐

 * pgcli：Postgres 命令行工具，具有自动补全和语法高亮功能。[链接](https://github.com/dbcli/pgcli) --推荐

 * try：很简单的命令行工具，用来试用python库。[链接](https://github.com/timofurrer/try) 

## 兼容性

帮助从 Python 2 向 Python 3迁移的库。

 * Python-Future：这就是 Python 2 和 Python 3 之间丢失的那个兼容性层。[链接](https://github.com/PythonCharmers/python-future) 

 * Python-Modernize：使 Python 代码更加现代化以便最终迁移到 Python 3。[链接]https://github.com/mitsuhiko/python-modernize) 

 * Six：Python 2 和 3 的兼容性工具。[链接](https://github.com/benjaminp/six) 

## 计算机视觉

计算机视觉库。

 * OpenCV：开源计算机视觉库。[链接](https://opencv.org/) 

 * pyocr：Tesseract 和 Cuneiform 的包装库。[链接](https://github.com/openpaperwork/pyocr) 

 * pytesseract：Google Tesseract OCR 的另一包装库。[链接](https://github.com/madmaze/pytesseract) 

 * SimpleCV：一个用来创建计算机视觉应用的开源框架。[链接](https://github.com/sightmachine/SimpleCV) 

## 并发和并行及异步与网络

用以进行并发和并行操作的库。

 * multiprocessing：(Python 标准库) 基于进程的“线程”接口。[链接](https://docs.python.org/2/library/multiprocessing.html)   --推荐

 * threading：(Python 标准库)更高层的线程接口。 [链接](https://docs.python.org/2/library/threading.html)　--推荐

 * eventlet：支持 WSGI 的异步框架。[链接](https://github.com/eventlet/eventlet/)

 * gevent：一个基于协程的 Python 网络库，使用greenlet。[链接](https://github.com/gevent/gevent)　--推荐

 * Tomorrow：用于产生异步代码的神奇的装饰器语法实现。 [链接](https://github.com/madisonmay/Tomorrow)　

 * uvloop：在libuv之上超快速实现asyncio事件循环。[链接](https://github.com/MagicStack/uvloop)　--推荐

 * asyncio - (Python 标准库) 异步 I/O, 事件循环, 协程以及任务 [链接](https://docs.python.org/3/library/asyncio.html)　--推荐

 * aiohttp 异步http client/server框架(asyncio) [链接](https://github.com/aio-libs/aiohttp)　--推荐

 * curio 协程并发库. [链接](https://github.com/dabeaz/curio)

 * pulsar - 事件驱动的并发框架. [链接](https://github.com/quantmind/pulsar)

 * pyzmq -  ZeroMQ 消息库的 Python 封装. [链接](https://github.com/zeromq/pyzmq/blob/master/docs/source/index.rst)

 * Twisted - 事件驱动的网络引擎. 和asyncio有很多类似的地方，逐渐被代替,需要数据库等相关生态圈的支持 [链接](https://github.com/twisted/twisted)

 * diesel - 基于Greenlet 的事件 I/O 框架。. [链接](https://github.com/dieseldev/diesel)

 * Tornado - web 框架和异步网络库. [链接](https://github.com/tornadoweb/tornado/blob/master/docs/index.rst)

 * Trio – 异步I/O [链接](https://github.com/python-trio/trio) 可能会飙升

 * NAPALM - 处理网络设备的跨供应API. [链接](https://github.com/napalm-automation/napalm)

 * txZMQ - 基于 Twisted 的 ZeroMQ 消息库的 Python 封装。[链接](https://github.com/smira/txZMQ)

## 配置

用来保存和解析配置的库。

 * config：logging 模块作者写的分级配置模块。[链接](https://pypi.python.org/pypi/config) -- 较长时间未更新

 * ConfigObj：INI 文件解析器，带验证功能。[链接](https://github.com/DiffSK/configobj)

 * ConfigParser：(Python 标准库) INI 文件解析器。[链接](https://docs.python.org/2/library/configparser.html)

 * profig：通过值转换配置多种格式。[链接](https://bitbucket.org/dhagrow/profig/)

 * python-decouple：将设置和代码完全隔离。[链接](https://github.com/henriquebastos/python-decouple)


## 加密

 * cryptography：这个软件包意在提供密码学基本内容和方法提供给 Python 开发者。[链接](https://github.com/pyca/cryptography/blob/master/docs/index.rst)

 * hashids：在 Python 中实现 hashids 。[链接](https://github.com/davidaurelio/hashids-python)

 * Paramiko：SSHv2 协议的 Python (2.6+, 3.3+) ，提供客户端和服务端的功能。[链接](https://github.com/paramiko/paramiko/) -- 推荐

 * Passlib：安全密码存储／哈希库，[链接](https://bitbucket.org/ecollins/passlib/overview)

 * PyCrypto：Python 密码学工具箱。[链接](https://github.com/dlitz/pycrypto)

 * PyNacl：网络和密码学(NaCl) 库的 Python 绑定。[链接](https://github.com/pyca/pynacl)

## 数据分析

 * blaze：NumPy 和 Pandas 的大数据接口。[链接](https://github.com/blaze/blaze)

 * Open Mining：使用 Python 挖掘商业情报 (BI) (Pandas web 接口)。[链接](https://github.com/mining/mining)

 * orange：通过可视化编程或 Python 脚本进行数据挖掘，数据可视化，分析和机器学习。[链接](https://github.com/biolab/orange3)

 * Pandas：提供高性能，易用的数据结构和数据分析工具。[链接](https://github.com/pandas-dev/pandas) --推荐

 * 书籍：利用Python进行数据分析 2017 第二版 中文 [链接](https://github.com/pandas-dev/pandas) --推荐

 * 书籍：利用Python进行数据分析 2017 第二版 代码 [链接](https://github.com/wesm/pydata-book)  --推荐

## 数据验证

数据验证库。多用于表单验证。


 * Cerberus： 轻量级可扩展的数据验证库.[链接](https://github.com/pyeve/cerberus/)

 * colander：验证并反序列化XML、JSON、HTML表单获取的数据。[链接](https://github.com/Pylons/colander/blob/master/docs/index.rst)

 * colander：json模式的实现。[链接](https://github.com/Julian/jsonschema)

 * kmatch：一种用于匹配/验证/筛选 Python 字典的语言。[链接]()

 * schema：一个用于对 Python 数据结构进行验证的库。[链接]()

 * Schematics：人性化的python数据结构。[链接](https://github.com/schematics/schematics)

 * valideer：轻量级可扩展的数据验证和适配库。[链接](https://github.com/podio/valideer)

 * voluptuous：Python 数据验证库。主要是为了验证传入 Python的 JSON，YAML 等数据。[链接](https://github.com/alecthomas/voluptuous)

## 数据可视化

进行数据可视化的库。 参见: [awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization)。

 
 * matplotlib：Python 2D 绘图库。[链接](https://github.com/matplotlib/matplotlib) --推荐

 * bokeh：用Python进行交互式web绘图。[链接](https://github.com/bokeh/bokeh) --推荐

 * ggplot：ggplot的 Python移植。[链接](https://github.com/yhat/ggpy) -荐

 * plotly：交互式基于浏览器的绘图。[链接](https://github.com/plotly/plotly.py)

 * pyecharts：基于百度 Echarts 的数据可视化库。[链接](https://github.com/pyecharts/pyecharts) -荐

 * pygal：Python SVG 图表创建工具。[链接](https://github.com/Kozea/pygal/blob/master/docs/index.rst)

 * pygraphviz：Graphviz 的 Python 接口。[链接](https://github.com/pygraphviz/pygraphviz)

 * PyQtGraph：交互式实时 2D/3D/ 图像绘制及科学/工程学组件。[链接](https://github.com/pyqtgraph/pyqtgraph)

 * SnakeViz：基于浏览器的 Python cProfile 模块输出结果查看工具。[链接](https://github.com/jiffyclub/snakeviz/)

 * vincent：把 Python 转换为 Vega 语法的转换工具。[链接](https://github.com/wrobstory/vincent)

 * VisPy：基于 OpenGL 的高性能科学可视化工具。[链接](https://github.com/vispy/vispy)

 * Altair - 用于Python的声明式统计可视化库。[链接](https://github.com/altair-viz/altair)

 * bqplot - Jupyter Notebook的互动绘图库。[链接](https://github.com/bloomberg/bqplot)

 * Seaborn - 使用Matplotlib进行统计数据可视化。[链接](https://github.com/mwaskom/seaborn) -荐

##动态消息

用来创建用户活动的库。

 * django-activity-stream：从你的站点行为中生成通用活动信息流。[链接](https://github.com/justquick/django-activity-stream)

 * Stream-Framework：使用 Cassandra 和 Redis 创建动态消息和通知系统。[链接](https://github.com/tschellenbach/Stream-Framework)


##　ORM

实现对象关系映射或数据映射技术的库。

### 关系型数据库

 * Django Models：Django 的一部分。[链接](https://docs.djangoproject.com/en/dev/topics/db/models/)

 * SQLAlchemy：Python SQL 工具以及对象关系映射工具。[链接](http://www.sqlalchemy.org/)

 * awesome-sqlalchemy系列 [链接](https://github.com/justquick/django-activity-stream)

 * Peewee：一个小巧，富有表达力的 ORM, 支持postgresql, mysql and sqlite。[链接]https://github.com/coleifer/peewee)

 * PonyORM：提供面向生成器的 SQL 接口的 ORM。[链接](https://github.com/ponyorm/pony/)

 * python-sql：编写 Python 风格的 SQL 查询。[链接](http://python-sql.tryton.org/)

### NoSQL 数据库

 * django-mongodb-engine：Django MongoDB 后端。[链接](https://github.com/django-nonrel/mongodb-engine)

 * PynamoDB：Amazon DynamoDB 的一个 Python 风格接口。[链接](https://aws.amazon.com/cn/dynamodb/)

 * flywheel：Amazon DynamoDB 的对象映射工具。[链接](https://github.com/stevearc/flywheel)

 * MongoEngine：Python 对象文档映射工具，用于 MongoDB。[链接](https://github.com/MongoEngine/mongoengine)

 * hot-redis：为 Redis 提供 Python 丰富的数据类型。[链接](https://github.com/stephenmcd/hot-redis)

 * redisco：一个 Python 库，提供可以持续存在在 Redis 中的简单模型和容器。[链接](https://github.com/kiddouk/redisco)

### 其他

 * butterdb：Google Drive 电子表格的 Python ORM。[链接](https://github.com/terrible-ideas/butterdb)

 * dataset ：基于JSON的数据库。[链接](https://github.com/pudo/dataset)


## 包管理

管理包和依赖的工具。


 * pip：Python 包和依赖关系管理工具。[链接](https://pypi.python.org/pypi)

 * pip-tools：保证 Python 包依赖关系更新的一组工具。[链接]https://github.com/jazzband/pip-tools)

 * conda：跨平台，Python 二进制包管理工具。[链接](https://github.com/conda/conda/)

 * Curdling：管理 Python 包的命令行工具。[链接](https://github.com/clarete/curdling)

 * wheel：Python 分发的新标准，意在取代 eggs。[链接](https://github.com/meshy/pythonwheels)


## 包仓库

本地 PyPI 仓库服务和代理。

 * warehouse：下一代 PyPI。[链接](https://github.com/pypa/warehouse)

 * Warehouse：[链接](https://pypi.org/)

 * bandersnatch：PyPA 提供的 PyPI 镜像工具。[链接](https://bitbucket.org/pypa/bandersnatch)

 * devpi：PyPI 服务和打包/测试/分发工具。[链接](https://github.com/devpi/devpi/)

 * localshop：本地 PyPI 服务（自定义包并且自动对 PyPI 镜像）。[链接](https://github.com/mvantellingen/localshop)


## 分发

打包为可执行文件以便分发。

 * PyInstaller：将 Python 程序转换成独立的执行文件（跨平台）。[链接](https://github.com/pyinstaller/pyinstaller)

 * dh-virtualenv：构建并将 virtualenv 虚拟环境作为Debian 包来发布。[链接](https://github.com/spotify/dh-virtualenv)

 * Nuitka：将脚本、模块、包编译成可执行文件或扩展模块。[链接](http://nuitka.net/)

 * py2app：将 Python 脚本变为独立软件包（Mac OS X）。[链接](https://bitbucket.org/ronaldoussoren/py2app)

 * py2exe：将 Python 脚本变为独立软件包（Windows）。[链接](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/) --已经比较久没有更新了。

 * pynsist：用来创建 Windows 安装程序的工具，可以在安装程序中打包 Python本身。[链接](https://github.com/takluyver/pynsist/blob/master/doc/index.rst)



## 文档

用以生成项目文档的库。

 * Sphinx：Python 文档生成器。[链接](https://github.com/sphinx-doc/sphinx/)

 * awesome-sphinxdoc：[链接](https://github.com/yoloseem/awesome-sphinxdoc)
    
 * MkDocs：对 Markdown 友好的文档生成器。[链接](https://github.com/mkdocs/mkdocs/) -- 推荐
    
 * pdoc：替换Epydoc 的库，可以自动生成 Python 库的 API 文档。[链接](https://github.com/BurntSushi/pdoc )
    
 * Pycco：文学编程风格的文档生成器。[链接](https://github.com/pycco-docs/pycco)
    
 * readthedocs：一个基于 Sphinx/MkDocs 的在线文档托管系统，对开源项目免费开放使用。[链接](https://github.com/rtfd/readthedocs.org/) -- 推荐

## 下载器

用来进行下载的库.

 * s3cmd：一个用来管理Amazon S3 和 CloudFront 的命令行工具。[链接](https://github.com/s3tools/s3cmd)

 * s4cmd：超级 S3 命令行工具，性能更加强劲。[链接](https://github.com/bloomreach/s4cmd)

 * you-get：YouTube/Youku/Niconico 视频下载器，使用 Python3 编写。[链接](https://github.com/soimort/you-get) --推荐

 * youtube-dl：一个小巧的命令行程序，用来下载 YouTube 视频。[链接](http://rg3.github.io/youtube-dl/)

## 电子商务

用于电子商务以及支付的框架和库。

 * django-oscar：基于Django 的开源的电子商务框架。[链接](https://github.com/django-oscar/django-oscar/) -- 推荐
    
 * django-shop： 基于 Django 的店铺系统。[链接](https://github.com/awesto/django-shop )
    
 * Cartridge：一个基于 Mezzanine 构建的购物车应用。[链接](https://github.com/stephenmcd/cartridge)
    
 * shoop：基于 Django 的开源电子商务平台。[链接](https://www.shuup.com/ )
    
 * alipay：非官方的 Python 支付宝 API。[链接](https://github.com/lxneng/alipay)
    
 * merchant：可以接收来自多种支付平台支付的 Django 应用。[链接](https://github.com/agiliq/merchant)
    
 * money：Python钱类，带有可选的CLDR支持的区域识别格式和可扩展的货币兑换解决方案。[链接](https://github.com/carlospalol/money)
    
 * forex-python：外汇汇率，比特币价格指数和货币兑换。[链接](https://github.com/MicroPyramid/forex-python)

 * saleor - Python和Django的电子商务店面。[链接](https://github.com/mirumee/saleor)

 * 雪峰磁针石说明:

python-currencies因为星级较少没有收录

## 编辑器插件

编辑器和 IDE 的插件

 * Elpy：Emacs Python 开发环境。[链接](https://github.com/jorgenschaefer/elpy)

 * SublimeJEDI：Sublime Text 插件，用来实现自动补全库 Jedi。[链接](https://github.com/srusskih/SublimeJEDI)

 * Anaconda：把你的 Sublime Text 3 变成功能齐全的 Python IDE。[链接](https://github.com/DamnWidget/anaconda)

 * YouCompleteMe：引入基于 Jedi 的 Python 自动补全引擎。[链接](https://github.com/Valloric/YouCompleteMe)

 * Jedi-vim：绑定 Vim 和 Jedi 自动补全库对 Python 进行自动补全。[链接](https://github.com/davidhalter/jedi-vim)

 * Python-mode：Vim 变成 Python IDE 的多合一插件。[链接](https://github.com/python-mode/python-mode)

 * PTVS：Visual Studio 的 Python 工具[链接](https://github.com/Microsoft/PTVS)

 * wingIDE：商业化的 Python IDE,功能强大，占用资源少，python开发。也有免费的社区版提供。[链接]https://wingware.com/) -- 推荐

 * PyCharm：商业化的 Python IDE ，由 JetBrains 开发。也有免费的社区版提供。[链接](https://www.jetbrains.com/pycharm/)

 * LiClipse：基于 Eclipse 的免费多语言 IDE 。使用 PyDev 来支持 Python 。[链接](http://www.liclipse.com/)
    
 * Spyder：开源 Python IDE。[链接](https://github.com/spyder-ide/spyder)

 * komodo-ide [链接](https://www.activestate.com/komodo-ide/python-editor)

## 电子邮件

用来发送和解析电子邮件的库。

 * mailer：用简单的方式发送邮件。[链接](https://pypi.python.org/pypi/mailer) -- 推荐

 * envelopes：人性化的电子邮件库。[链接](https://github.com/tomekwojcik/envelopes/)
    
 * flanker：email 地址和 Mime 解析库。[链接](https://github.com/mailgun/flanker)

 * imbox：人性化的Python IMAP 库[链接](https://github.com/martinrusev/imbox)

 * inbox.py：人性化的Python SMTP 服务器。[链接](https://github.com/kennethreitz/inbox.py)

 * inbox：具有时尚API的IMAP/SMTP同步系统。[链接](https://github.com/nylas/sync-engine) -- 推荐

 * lamson：Python 风格的 SMTP 应用服务器。[链接](https://github.com/zedshaw/lamson)

 * marrow.mailer：高性能可扩展邮件分发框架。[链接](https://github.com/marrow/mailer)

 * modoboa：一个邮件托管和管理平台，具有现代的、简约的 Web UI。[链接](https://github.com/modoboa/modoboa)

 * pyzmail：创建，发送和解析电子邮件。[链接](https://pypi.python.org/pypi/pyzmail)

 * Talon：Mailgun 库，用来抽取信息和签名。[链接](https://github.com/mailgun/talon)

## 特殊文本格式处理

一些用来解析和操作特殊文本格式的库。

### 通用
        
 * tablib：处理 XLS, CSV, JSON, YAML表格数据的模块。[链接](https://github.com/kennethreitz/tablib)

### Office
        
 * Marmir：把输入的Python 数据结构转换为电子表单。[链接](https://github.com/brianray/mm)
        
 * openpyxl：用来读写 Excel 2010 xlsx/xlsm/xltx/xltm 文件的库。[链接](https://bitbucket.org/openpyxl/openpyxl)
        
 * python-docx：读取，查询以及修改 Microsoft Word 2007/2008 docx 文件。[链接](https://github.com/python-openxml/python-docx)
        
 * unoconv：在 LibreOffice/OpenOffice 支持的任意文件格式之间进行转换。[链接](https://github.com/dagwieers/unoconv)
        
 * XlsxWriter：一个用于创建 Excel .xlsx 文件的 Python 模块。[链接](https://github.com/jmcnamara/XlsxWriter)
        
 * xlwings：一个使得在 Excel 中方便调用 Python 的库（反之亦然），基于 BSD 协议。[链接](https://github.com/zoomeranalytics/xlwings)
        
 * xlwt/xlrd：读写 MS Excel 97/2000/XP/2003 XLS  Excel 文件的数据和格式信息。[链接](https://github.com/python-excel/xlrd)
        
 * relatorio：输出odt和pdf的模板。[链接](https://pypi.python.org/pypi/relatorio)

 * pyexcel：用于读取，操作和写入CSV，ODS，XLS，XLSX和XLSM文件数据的单一API。[链接](https://github.com/pyexcel/pyexcel)

-- 实际pandas为第一数据处理库，支持所有excel格式。
        
### PDF

 * PDFMiner：从PDF文档中抽取信息的工具。[链接](https://github.com/euske/pdfminer)
        
 * PyPDF2：可以分割，合并和转换 PDF 页面的库。[链接](https://github.com/mstamy2/PyPDF2)
        
 * ReportLab：快速创建富文本 PDF 文档。[链接](http://www.reportlab.com/opensource/)
    
### Markdown
        
 * Mistune：快速并且功能齐全的纯 Python 实现的 Markdown 解析器。[链接](https://github.com/lepture/mistune)
        
 * Python-Markdown：John Gruber’s Markdown 的 Python 版实现。[链接](https://github.com/waylan/Python-Markdown)
        
 * Python-Markdown2：纯 Python 实现的 Markdown 解析器，比 Python-Markdown 更快，更准确，可扩展。[链接](https://github.com/trentm/python-markdown2)

### YAML
        
 * PyYAML：Python 版本的 YAML 解析器。[链接](https://github.com/yaml/pyyaml)

### CSV
        
 * csv: 标准库，csv文件读写。[链接](https://docs.python.org/2/library/csv.html)

 * csvkit：用于转换和操作 CSV 的工具。[链接](https://github.com/wireservice/csvkit)
    
Archive
        
 * unp：方便解包归档文件的命令行工具。[链接](https://github.com/mitsuhiko/unp)

## 文本处理

用于解析和操作文本的库。


### 通用

 * chardet：字符编码检测器，兼容 Python2 和 Python3。[链接](https://github.com/chardet/chardet)

 * difflib：(Python 标准库)帮助我们进行差异化比较。[链接](https://docs.python.org/2/library/difflib.html)

 * ftfy：让Unicode文本更完整更连贯。[链接](https://github.com/LuminosoInsight/python-ftfy)

 * fuzzywuzzy：模糊字符串匹配。[链接](https://github.com/seatgeek/fuzzywuzzy) --推荐

 * Levenshtein：快速计算编辑距离以及字符串的相似度。[链接](https://github.com/ztane/python-Levenshtein/)

 * pyfiglet：pyfiglet -figlet 的 Python实现。[链接](https://github.com/pwaller/pyfiglet)

 * shortuuid：生成器库，用以生成简洁的，明白的，URL 安全的 UUID。[链接](https://github.com/skorokithakis/shortuuid)

 * unidecode：Unicode 文本的 ASCII 转换形式 。[链接](https://github.com/avian2/unidecode)

 * uniout：打印可读的字符，而不是转义的字符串。[链接](https://github.com/moskytw/uniout)

 * xpinyin：把汉字转换为拼音的库。[链接](https://github.com/lxneng/xpinyin)

 * pypinyin ：把汉字转换为拼音的库。[链接](https://github.com/mozillazg/python-pinyin)

 * simplejson：Python的JSON编码、解码器。[链接](https://github.com/simplejson/simplejson)

### Slugify

 * awesome-slugify：一个 Python slug 化库，可以保持 Unicode。[链接](https://github.com/dimka665/awesome-slugify)

 * python-slugify：Python slug 化库，可以把 unicode 转化为 ASCII。[链接](https://github.com/un33k/python-slugify)

 * unicode-slugify：slug 工具，可以生成 unicode slugs ,需要依赖 Django 。[链接](https://github.com/mozilla/unicode-slugify)

### 解析器

 * phonenumbers：解析，格式化，储存，验证国际电话号码。[链接](https://github.com/daviddrysdale/python-phonenumbers)

 * PLY：lex 和 yacc 解析工具的 Python 实现。[链接](https://github.com/dabeaz/ply)

 * Pygments：通用语法高亮工具。[链接](https://bitbucket.org/birkenfeld/pygments-main) --强烈推荐

 * pyparsing：生成通用解析器的框架。[链接](https://sourceforge.net/projects/pyparsing/)

 * python-nameparser：把人名分解为几个独立的部分。[链接](https://github.com/derek73/python-nameparser)

 * python-user-agents：浏览器 user agent 解析器。[链接](https://github.com/selwin/python-user-agents)

 * sqlparse：无验证的 SQL 解析器。官网[链接](https://github.com/andialbrecht/sqlparse)


## 第三方 API

用来访问第三方 API的库。 参见： List of Python API Wrappers and Libraries。 [链接](https://github.com/realpython/list-of-python-api-wrappers)

 * apache-libcloud：为各种云设计的 Python 库。[链接](https://github.com/apache/libcloud)

 * boto3：Amazon Web Services 的 Python 接口。[链接](https://github.com/boto/boto3)

 * django-wordpress：WordPress models and views for Django.[链接](https://github.com/istrategylabs/django-wordpress)

 * facebook-sdk：Facebook 平台的 Python SDK.[链接](https://github.com/mobolic/facebook-sdk)

 * facepy：Facepy 让和 Facebook's Graph API 的交互变得更容易。[链接](https://github.com/jgorset/facepy)

 * gmail：Gmail 的 Python 接口。[链接](https://github.com/charlierguo/gmail)

 * google-api-python-client：Python 用的 Google APIs 客户端库。[链接](https://github.com/google/google-api-python-client)

 * gspread：Google 电子表格的 Python API.[链接](https://github.com/burnash/gspread)

 * twython：Twitter API 的封装。[链接](https://github.com/ryanmcgrath/twython)

## URL处理

解析URLs的库

 * furl：处理 URL 更简单小型 Python 库。[链接](https://github.com/gruns/furl)

 * purl：简单的，不可变的URL类，具有简洁的 API 来进行询问和处理。[链接](https://github.com/codeinthehole/purl)

 * pyshorteners：纯 Python URL 缩短库。[链接](https://github.com/ellisonleao/pyshorteners)

 * shorturl：生成短小 URL 和类似 bit.ly 短链的Python 实现。[链接](https://github.com/Alir3z4/python-short_url)

 * webargs：解析 HTTP 请求参数的库，内置对流行 web 框架的支持，包括 Flask, Django, Bottle, Tornado和 Pyramid。[链接](https://github.com/sloria/webargs)



## Video

用来操作视频和GIF的库。

 * moviepy：一个用来进行基于脚本的视频编辑模块，适用于多种格式，包括动图 GIFs。[链接](https://github.com/Zulko/moviepy/)

## WSGI 服务器

兼容 WSGI 的 web 服务器

 * gunicorn：Pre-forked, 部分是由 C 语言编写的。[链接](https://github.com/benoitc/gunicorn/) --推荐

 * uwsgi：uwsgi 项目的目的是开发一组全栈工具，用来建立托管服务， 由 C 语言编写。[链接](https://github.com/unbit/uwsgi-docs/blob/master/index.rst)

 * bjoern：异步，非常快速，由 C 语言编写。[链接](https://github.com/jonashaag/bjoern)

 * fapws3：异步 (仅对于网络端)，由 C 语言编写。[链接](https://github.com/william-os4y/fapws3)

 * meinheld：异步，部分是由 C 语言编写的。[链接](https://github.com/mopemope/meinheld)

 * netius：异步，非常快速。[链接](https://github.com/hivesolutions/netius)

 * paste：多线程，稳定，久经考验。[链接](https://bitbucket.org/ianb/paste)　--推荐

 * waitress：多线程, 是它驱动着 Pyramid 框架。[链接](https://github.com/Pylons/waitress/blob/master/docs/index.rst)

 * Werkzeug：一个 WSGI 工具库，驱动着 Flask ，而且可以很方便大嵌入到你的项目中去。[链接](https://github.com/pallets/werkzeug)　--推荐


## 网页内容提取

用于进行网页内容提取的库。

  * Haul：可以扩展的图像爬取工具。[链接](https://github.com/vinta/Haul) 

  * html2text：将 HTML 转换为 Markdown 格式文本[链接](https://github.com/Alir3z4/html2text) 

  * lassie：人性化的网页内容检索库。[链接](https://github.com/michaelhelmick/lassie) 

  * micawber：一个小型网页内容提取库，用来从 URLs 提取富内容。[链接](https://github.com/coleifer/micawber) 

  * newspaper：使用 Python 进行新闻提取，文章提取以及内容策展。[链接](https://github.com/codelucas/newspaper) --推荐

  * opengraph：用来解析开放图形协议的 Python模块。[链接](https://github.com/erikriver/opengraph) 

  * python-goose：HTML内容/文章提取器。[链接](https://github.com/grangier/python-goose) 

  * python-readability：arc90的易读性工具的移植。[链接](https://github.com/buriy/python-readability) 

  * sumy：一个为文本文件和 HTML 页面进行自动摘要的模块。[链接](https://github.com/miso-belica/sumy) 

  * textract：从任何格式的文档中提取文本，Word，PowerPoint，PDFs 等等。[链接](https://github.com/deanmalmgren/textract) 



## 网络爬虫

  * Scrapy：快速高级的屏幕爬取及网页采集框架。[链接](https://github.com/scrapy/scrapy) --强烈推荐

  * cola：高层分布式爬虫框架。[链接](https://github.com/chineking/cola) 

  * Demiurge：基于PyQuery 的爬虫微型框架。[链接](https://github.com/matiasb/demiurge) 

  * feedparser：通用 feed 解析器。[链接](https://github.com/kurtmckee/feedparser) 

  * Grab：站点爬取框架。[链接](https://github.com/lorien/grab/) 

  * MechanicalSoup：用于自动和网络站点交互的 Python 库。[链接](https://github.com/MechanicalSoup/MechanicalSoup) 

  * portia：Scrapy 可视化爬取。[链接](https://github.com/scrapinghub/portia) --推荐

  * pyspider：一个强大的爬虫系统。[链接](https://github.com/binux/pyspider) --强烈推荐

  * RoboBrowser：一个简单的，Python 风格的库，用来浏览网站，而不需要一个独立安装的浏览器。[链接](https://github.com/jmcarp/robobrowser) 

  * MechanicalSoup：用于自动和网络站点交互的 Python 库。[链接](https://github.com/MechanicalSoup/MechanicalSoup) 



## Web 框架

全栈 Web 框架。

 * Django：Python 界最流行的 web 框架。[链接](https://github.com/django/django) wesome-django系列 [链接](https://github.com/rosarior/awesome-django) --强烈推荐

 * Flask：Python 微型框架。[链接](https://github.com/pallets/flask)  awesome-flask系列 [链接](https://github.com/humiaozuzu/awesome-flask) --强烈推荐 python web框架第一名

 * pyramid：一个小巧，快速，接地气的开源Python web 框架。[链接](https://github.com/Pylons/pyramid/) 
        awesome-pyramid系列 [链接](https://github.com/uralbash/awesome-pyramid) 

 * Bottle：一个快速小巧，轻量级的 WSGI 微型 web 框架。[链接](https://github.com/bottlepy/bottle)  --推荐

 * CherryPy：一个极简的 Python web 框架，支持HTTP/1.1 协议且具有WSGI 线程池。[链接](https://github.com/cherrypy/cherrypy) 

 * sanic：python3 快速的web服务器，类似flask。[链接](https://github.com/channelcat/sanic) --推荐

 * web.py：既简单，又强大的web 框架。[链接](https://github.com/webpy/webpy/tree/master) 

 * TurboGears：易于扩展的全栈微框架。[链接](https://github.com/TurboGears/tg2) 

 * web2py：全栈 web 框架和平台，用于安全数据库访问的web用。[链接](https://github.com/web2py/web2py) 

 * Tornado - web 框架和异步网络库. [链接](https://github.com/tornadoweb/tornado/blob/master/docs/index.rst)



## WebSocket

 * AutobahnPython：WebSocket & WAMP 基于 Twisted 和 asyncio。[链接](https://github.com/crossbario/autobahn-python)
 
 * Crossbar：开源统一应用路由(Websocket & WAMP for Python on Autobahn).[链接](https://github.com/crossbario/crossbar/) 

 * django-channels：Django异步。[链接](https://github.com/django/channels) 

 * django-socketio：Django WebSocket。[链接](https://github.com/stephenmcd/django-socketio)

 * WebSocket-for-Python：为Python2/3 以及 PyPy 编写的 WebSocket 客户端和服务器库。[链接](https://github.com/Lawouach/WebSocket-for-Python) 

### 持续更新


交流QQ群：python 测试开发 144081101

wechat： pythontesting

淘宝天猫可以把链接发给qq850766020，为你生成优惠券，降低你的购物成本！

快来领取支付宝跨年红包！1月1日起还有机会额外获得专享红包哦！复制此消息，打开最新版支付宝就能领取！2C56CV70sA
