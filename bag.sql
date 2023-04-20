PGDMP     3                    {         	   komunalka    15.2    15.2 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398 	   komunalka    DATABASE     }   CREATE DATABASE komunalka WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE komunalka;
                postgres    false            �            1259    16411    accruals    TABLE       CREATE TABLE public.accruals (
    number_ls integer NOT NULL,
    accrual_date date NOT NULL,
    accrual_hvs numeric,
    accrual_gvs_heat_carrier numeric,
    accrual_gvs_thermal_energy numeric,
    accrual_total_gvs numeric,
    accrual_ee numeric,
    total_accrual numeric
);
    DROP TABLE public.accruals;
       public         heap    postgres    false            �            1259    16399 	   customers    TABLE       CREATE TABLE public.customers (
    number_ls integer NOT NULL,
    indications_date date NOT NULL,
    indications_hvs numeric,
    indications_gvs numeric,
    indications_ee_daytime numeric,
    number_of_residents integer,
    indications_ee_night numeric
);
    DROP TABLE public.customers;
       public         heap    postgres    false            �          0    16411    accruals 
   TABLE DATA           �   COPY public.accruals (number_ls, accrual_date, accrual_hvs, accrual_gvs_heat_carrier, accrual_gvs_thermal_energy, accrual_total_gvs, accrual_ee, total_accrual) FROM stdin;
    public          postgres    false    215   �       �          0    16399 	   customers 
   TABLE DATA           �   COPY public.customers (number_ls, indications_date, indications_hvs, indications_gvs, indications_ee_daytime, number_of_residents, indications_ee_night) FROM stdin;
    public          postgres    false    214   w       k           2606    16417    accruals accruals_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.accruals
    ADD CONSTRAINT accruals_pkey PRIMARY KEY (number_ls, accrual_date);
 @   ALTER TABLE ONLY public.accruals DROP CONSTRAINT accruals_pkey;
       public            postgres    false    215    215            i           2606    16407    customers customers_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (number_ls, indications_date);
 B   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    214    214            �   �   x�����0E�v/�H_��&� ��A8@6`���߳��Nl�ͷ�����6�`��z�w���2E�;k�gP��� �h���R�~*Q�d̪cyȃE�
�_�E�!�0��������(]'
���K+{[�l4~�'�h�7�u9�1�,��e���L��;�T�       �   T  x���ۑ�0��c/gGn�6����X�.Dd������O�?W����
P����g98��^@��h@���"6�#'.$�������1^G�P�4�f��
�J;�8�@Oc*d{0P}�=� cx�H5�.�)����2+����͟k�M�$�r��B<G`�6�� �y�bM�����_%נ�\�[��{�1�8�/i�.a��?������k���@E���4���d � �?��o�% ��� A���#˟`�e}�t��R�~�
C��%�|�l4�0�	�'�<��d #�u2`x��L�N�>�_&&�q�8�y����xA��Y���KRN     