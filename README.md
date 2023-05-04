![](static/logo.png)

# FeelGood

使用 FastAPI + SQLAchemy 构建一个数据管理后端系统

## 安装依赖

```shell
pip3 install -r requirements.txt
```

## 启动服务

```shell
python3 feelgood.py
```

或者

```shell
uvicorn feelgood:app --reload
```

## OpenAPI文档

开发环境：

```shell
127.0.0.1:8000/docs
```

## 数据库迁移：
```shell
# 自动生成迁移文件
alembic revision --autogenerate -m "描述"
# 执行迁移
alembic upgrade head
```

## admin前端打包：

```shell
cd fadmin
npm install --registry=https://registry.npm.taobao.org
npm run build:prod
```

