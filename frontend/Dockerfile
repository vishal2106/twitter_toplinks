# pull official base image
FROM node:8
RUN npm install -g serve
COPY package.json package.json
RUN npm install 
COPY . .
RUN npm run dev
CMD serve -p $PORT -s public
