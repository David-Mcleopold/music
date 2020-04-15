"""
Django settings for music project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ugw(znkxi@=juglpj=khx79k4(*)&e_ono&nk=ox38tiqh=vyb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
    'ranking',
    'user',
    'play',
    'search',
    'comment',
    # 添加验证码功能
    'captcha'
]

# django_simple_captcha 验证码基本配置
# 设置验证码的显示顺序，一个验证码识别包含文本输入框、隐藏域和验证码图片，该配置是设置三者的显示顺序
CAPTCHA_OUTPUT_FORMAT = '%(text_field)s %(hidden_field)s %(image)s'
# 设置图片噪点
CAPTCHA_NOISE_FUNCTIONS = ( # 设置样式
                            'captcha.helpers.noise_null',
                            # 设置干扰线
                           'captcha.helpers.noise_arcs',
                            # 设置干扰点
                           'captcha.helpers.noise_dots',
                           )
# 图片大小
CAPTCHA_IMAGE_SIZE = (100, 25)
# 设置图片背景颜色
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
# 图片中的文字为随机英文字母，如 mdsh
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为英文单词
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'
# 图片中的文字为数字表达式，如1+2=</span>
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# 设置字符个数
CAPTCHA_LENGTH = 4
# 设置超时(minutes)
CAPTCHA_TIMEOUT = 1


# 添加中间件LocaleMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 使用中文
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'music.urls'

# 设置模版路径，在每个App里分别创建模版文件夹templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'index/templates'),
                 os.path.join(BASE_DIR, 'ranking/templates'),
                 os.path.join(BASE_DIR, 'user/templates'),
                 os.path.join(BASE_DIR, 'play/templates'),
                 os.path.join(BASE_DIR, 'comment/templates'),
                 ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'music.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# 设置数据库连接信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_db',
        'USER': 'root',
        'PASSWORD': '1234567',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 配置自定义用户表MyUser
AUTH_USER_MODEL = 'user.MyUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# STATIC_ROOT用于项目部署上线的静态资源文件
# STATIC_ROOT = 'D:/MyProgramFiles/DjangoProj/music/static'
STATIC_URL = '/static/'
# STATICFILES_DIRS用于收集admin的静态资源文件
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
