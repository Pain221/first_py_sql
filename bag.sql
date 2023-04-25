PGDMP                         {         	   komunalka    15.2    15.2 
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
    public          postgres    false    214   <       k           2606    16417    accruals accruals_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.accruals
    ADD CONSTRAINT accruals_pkey PRIMARY KEY (number_ls, accrual_date);
 @   ALTER TABLE ONLY public.accruals DROP CONSTRAINT accruals_pkey;
       public            postgres    false    215    215            i           2606    16407    customers customers_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (number_ls, indications_date);
 B   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    214    214            �   q  x��VYn�0�V�R�;�K����xc;�M�:���ᐊ��ESV�`�Pn���l��i�A�MU���[��+���٨;��%��?4�)F�2=����$�M#x>�Z���4/��&ZA,c��@��YωX?&*ޫ`�I�\YPD��4M*���\��uO���:�O2�|�cp�]��J!�3=j*إ8�Ӛ��"���H*��^"�N���,����i�iPm2�����H��T� �D'P	#�`����dc~�cIddz�(|�_�Х�N�rW©x���w�OT�ei��jľ*P�/�Ƞjfdq_爯�OH"¶�JWB{l�
���	?P���KU���N̕|�����1�Zwz�1�܊]��͵(��B�TcZ�UOI��v:y«h�)d��U��Q�L%�L�~>���Sa�6W'����yl򁱔-;��mx���^����yPN�:�{FN��0ZF7�;�g?ƱN���ݏ�������˧�lj�9G�7����XR���"4umpU�՜��|��a��{\��7)�;�7=�D=b�e������g6�1w�y�X'b�_�ͣ���E�w���<�c����4���$��G�i�H
GCtY.�O�\.���:Y      �   y  x��V�q� ����;�L���_G�9�!ːx�VZ�� ������?p� X����}.�A �a4�� ��"n8�8q )��pq����4<����!�Z���7��D58�~�)P3��@=�o�KN�`� g�TC.B5�+�TͿȼ�q��XrS��_qծQ<K��9�� O?��bt	��i��V��x�>D��_��ݠ���B|�8IP�C�f�#~����K����ק��>� y F+�"��ar��sSa_��P����t� ���@�Am��teTP���˱��i�$]�C�)&�[�h�"7�_����S��c� �Οq�� �)p�F$>�i��k<�z.ܿ�w7�i���%��{�U�
�n��G�n;��?�ɝ8a��t+��<�M6�:�M�h'��G0�m"np���y�O'�ގ4�/hf�hܙF0җ;��Y�2L���� ��ԧ�/���}��ދ٭O�zi�<&�O��'G��=�Q}U ��#w�V�K��eӴ���*@�4ME�MW���>L�i2s��]6%�۷�T��[����_�����Sz�ţƽ8����./ܼ�uX��9t������`s~�t��Ԧ��Ȫ�����N�rz���|>��Z�     