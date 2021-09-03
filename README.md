# flask-demo

Flask脚手架

# 环境

- Python-3.7.10
    - Flask==1.1.4
    - SQLAlchemy==1.4.22
    - PyMySQL==1.0.2

# 文件组织结构

待完善

# 项目特点

1. 利用蓝图构建类似Django路由结构

2. 利用Flask请求上下文制作 RequestMiddleware类: `core.request_middlewares.base`

3. 代理模式解决日志不打印问题：`libs.logger`
