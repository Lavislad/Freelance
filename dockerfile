FROM nginx as production

COPY ./nginx/default.conf /etc/nginx/conf.d

COPY ./ /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
