PGDMP                       |        	   Contactos    16.2    16.2 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16760 	   Contactos    DATABASE     �   CREATE DATABASE "Contactos" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "Contactos";
                postgres    false            �            1259    16762 	   Contactos    TABLE     �   CREATE TABLE public."Contactos" (
    "Id_Contacto" integer NOT NULL,
    "Nombre" character varying(50),
    "Direccion" text,
    "Telefono" numeric(8,0),
    "Email" character varying
);
    DROP TABLE public."Contactos";
       public         heap    postgres    false            �            1259    16761    Contactos_Id_Contacto_seq    SEQUENCE     �   ALTER TABLE public."Contactos" ALTER COLUMN "Id_Contacto" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Contactos_Id_Contacto_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    216            �          0    16762 	   Contactos 
   TABLE DATA           `   COPY public."Contactos" ("Id_Contacto", "Nombre", "Direccion", "Telefono", "Email") FROM stdin;
    public          postgres    false    216   M	       �           0    0    Contactos_Id_Contacto_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public."Contactos_Id_Contacto_seq"', 1, true);
          public          postgres    false    215            Q           2606    16768    Contactos Contactos_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public."Contactos"
    ADD CONSTRAINT "Contactos_pkey" PRIMARY KEY ("Id_Contacto");
 F   ALTER TABLE ONLY public."Contactos" DROP CONSTRAINT "Contactos_pkey";
       public            postgres    false    216            �   y   x�̽
�0�9y��B0�ь�H����\�K����T���|�85Je��$��L�p�)��U�i�Sb�����9΄��.��\nEB�*�{��"����y�W�-���B1�I��Z�g%T     