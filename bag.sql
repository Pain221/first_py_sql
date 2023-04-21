PGDMP     9        
            {         	   komunalka    15.2    15.2 
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
    public          postgres    false    214   �       k           2606    16417    accruals accruals_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.accruals
    ADD CONSTRAINT accruals_pkey PRIMARY KEY (number_ls, accrual_date);
 @   ALTER TABLE ONLY public.accruals DROP CONSTRAINT accruals_pkey;
       public            postgres    false    215    215            i           2606    16407    customers customers_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (number_ls, indications_date);
 B   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    214    214            �     x��U�m�0�Vv)�7�%:A���;�m�M��F�@�H�<H��X4e�����y�������H�o2��blOo�BlC�t�g��=rKh�xi(S��g���cH'1m�땷�:�1м�3�h�����=��\��9Q�Nro��B(E4�IӤ�oh�p��b]���Oj� K�dR�J�����N+��ϲ�TpJq��Z��J۵$�#���k�\;�VW��;�r���A����R���K�jh����f���`��j��jľUY�!2����6q�E���!J�����Jh��5��D�ڱLhF	�;)� b9��.;[����|�T��/E�~Π֝�}����v4��H��c�~?�4�S�e!��0���=��G����-;�����YԳ����ؒ[O:)'�$�S`.f��/
�3�y�y2�Ǻ�NΘ^�6�@���Rv��9����¬��jO��`|���
�x����=�N[J���PZݸQq���M0�Ǻ��Fpŝֆ���7=r��g�~��].��6��      �   �  x���[��0���^:Gn�nbV���c�i�����>����K�#�v~���`�߿zo�ap&�j�0�l�{���;�'��������$�<�\�p*���b��֊h��waJ�Ng���y���+@+�j�U�� �4T��	2?s4��km���W����t��Xf�{���Qb����UihP� ��1�:_��є�p�:�~��$�oH���?fФ|�|N��*QU��K���Ec���y�����iw	:	\�>���0�YA�7_�g2K"9��0��R���w�#By��7p�A3�}1 �\?�3xn���٬H���">/�j��y?�6H;.��L���uJ�w�	����o���hK��~C����/���<�7����݀�u�Ν�r#O=�-/Ay�H��}���mLG>C�G�@�W��L�lFb��7��Zk��{:�[߫1S��h��/�p�?C^�i{�l��y��{     