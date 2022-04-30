FROM python:3.10.4-alpine3.15
ENV PROJECT_DIR=/opt/ssh

COPY requirements.txt $PROJECT_DIR/
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev libressl-dev && \
    pip install -r $PROJECT_DIR/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    apk --purge del .build-deps && \
    rm -rf /var/cache/apk/*

COPY . $PROJECT_DIR

ENTRYPOINT ["python", "/opt/ssh/main.py"]
