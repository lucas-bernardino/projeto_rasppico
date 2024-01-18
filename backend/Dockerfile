FROM node:alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . ./

RUN npm install -g nodemon

EXPOSE 3001

CMD [ "npm", "run", "server" ]
