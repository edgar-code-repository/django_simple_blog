DJANGO BLOG APP
---------------------------------------------------------------------------------------------------------------------

Sencillo blog desarrollado con Django 2.2.4 y Bootstrap 4.

La aplicación se conecta a una base de datos PostgreSQL utilizando las librerias psycopg2 y dj_database_url.


---------------------------------------------------------------------------------------------------------------------

Se configuran models para ser utilizados desde la aplicación admin que provee Django,
modificando archivo admin.py:

```

admin.site.register(Technology, TechnologyModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)

```

---------------------------------------------------------------------------------------------------------------------

**Creación de un Post desde la aplicación admin:**

![Screenshot AdminsPostCreate](screenshots/blog_add_post.png)

---------------------------------------------------------------------------------------------------------------------

**Despliegue de posts en página principal:**

![Screenshot BlogMainPage](screenshots/blog_main.png)



---------------------------------------------------------------------------------------------------------------------