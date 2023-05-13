from fadmin.db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean, Float


class AppName(Base):
    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(20), index=True, comment="应用名称")
    package = Column(String(100), comment="包名")
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now)


class Framework(Base):
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(20), index=True, comment="架构")
    description = Column(String(1000), comment="描述")
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now)


class Scene(Base):
    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(20), ForeignKey("appname.app_name"), index=True, comment="应用名称")
    frame_work = Column(String(20), ForeignKey("framework.platform"), index=True, comment="架构")
    scene = Column(String(100), comment="场景")
    description = Column(String(1000), comment="描述")
    is_online = Column(Boolean, comment="是否上线")
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now)


class PerfData(Base):
    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(20), ForeignKey("appname.app_name"), index=True, comment="应用名称")
    frame_work = Column(String(20), ForeignKey("framework.platform"), index=True, comment="架构")
    scene = Column(String(100), ForeignKey("scene.scene"), comment="场景")
    number = Column(Integer, comment="次数")
    test_time = Column(DateTime(), comment="测试时间")
    report_url = Column(String, comment="测试报告url")
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now)


class TestApplicationVersion(Base):
    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(20), ForeignKey("appname.app_name"), index=True, comment="应用名称")
    frame_work = Column(String(20), ForeignKey("framework.platform"), index=True, comment="架构")
    version = Column(String(20), comment="版本")
    test_time = Column(DateTime(), comment="测试时间")
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now)


class PerfDataDay(Base):
    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(20), ForeignKey("appname.app_name"), index=True, comment="应用名称")
    frame_work = Column(String(20), ForeignKey("framework.platform"), index=True, comment="架构")
    scene = Column(String(100), ForeignKey("scene.scene"), comment="场景")
    time_consume = Column(Float, comment="耗时")
    test_time = Column(DateTime(), comment="测试时间")
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now)


class TemporaryTable(Base):
    """临时表"""
    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(20), ForeignKey("appname.app_name"), index=True, comment="应用名称")
    frame_work = Column(String(20), ForeignKey("framework.platform"), index=True, comment="架构")
    scene = Column(String(100), ForeignKey("scene.scene"), comment="场景")
    number = Column(Integer, comment="次数")
    test_time = Column(DateTime(), comment="测试时间")
    report_url = Column(String, comment="测试报告url")
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now)
