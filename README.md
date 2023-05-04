![](static/logo.png)

# FeelGood（FastAPI-Xadmin）

使用 FastAPI + SQLAchemy  + Vue + Element UI 构建的后台管理系统。

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
IP:8000/docs
```

## 数据库迁移
```shell
# 自动生成迁移文件
alembic revision --autogenerate -m "描述"
# 执行迁移
alembic upgrade head
```

## Admin前端

开发环境：

```python
cd fadmin
# 安装依赖
npm install --registry=https://registry.npm.taobao.org
# 启动开发环境
npm run dev
```

打包：

```shell
npm run build:prod
```

