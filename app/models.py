# coding: utf-8

from datetime import datetime
from enum import IntEnum, unique

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql.types import TINYINT

from libs.uuid import make_uuid

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 't_user'
    __table_args__ = {'comment': '用户表'}

    @unique
    class UserTypeEnum(IntEnum):
        """用户类型枚举类"""
        NORMAL = 1  # 普通用户
        VIP = 2  # VIP

    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True, comment='表id')
    user_id = db.Column(db.CHAR(length=32), nullable=False, default=make_uuid, comment='用户id', unique=True)
    user_type = db.Column(TINYINT, nullable=False, default=UserTypeEnum.NORMAL.value, comment='用户类型')
    name = db.Column(db.VARCHAR(length=50), nullable=False, default='', comment='名称', unique=True)
    is_deleted = db.Column(TINYINT, nullable=False, default=1, comment='是否已删除：0未删除 1已删除')
    create_time = db.Column(db.DATETIME, nullable=False, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')
