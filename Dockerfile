FROM node:20.9
# node의 20.9버전으로 부터 만들겠다
RUN mkdir /app/
# root에 app이라는 폴더를 만들겠다
WORKDIR /app/
# 내가 작업할 디렉토리를 app이라고 하겠다 (소스코드를 app에 넣겠다)
COPY package*.json /app/

RUN npm install

RUN npm install -g nodemon

COPY ./ /app/

EXPOSE 8080
# 8080 포트를 외부로 노출 시키겠다.
CMD ["npm", "run", "dev"]