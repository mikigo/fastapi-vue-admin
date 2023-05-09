# fastapi-vue-admin

使用 FastAPI + SQLAchemy  + Vue + Element UI 构建的后台管理系统。

## 安装依赖

提供多种环境安装方式；

（1）本机安装：

```shell
pip3 install -r requirements.txt
```

（2）Python 虚拟环境安装：

- pipenv

  ```shell
  pipenv install
  ```

- poetry

  ```shell
  poetry install
  ```

（3）Docker

- 待定。。

## 启动服务

```shell
python3 main.py
```

或者

```shell
uvicorn main:app --reload
```

服务启动之后根据终端提示在浏览器访问；

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

## 后台管理系统

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

