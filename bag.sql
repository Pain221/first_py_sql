PGDMP                         {         	   komunalka    15.2    15.2 
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
    public          postgres    false    214   <       k           2606    16417    accruals accruals_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.accruals
    ADD CONSTRAINT accruals_pkey PRIMARY KEY (number_ls, accrual_date);
 @   ALTER TABLE ONLY public.accruals DROP CONSTRAINT accruals_pkey;
       public            postgres    false    215    215            i           2606    16407    customers customers_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (number_ls, indications_date);
 B   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    214    214            �   q  x��VYn�J���2Dsg_bN0�?ǫ�"�e%�##@�^���dfV_���j�K������G8�q�'��{KJ��_-aLM;kʸ�֔���ǻA��S�F���Y��+эXe���ܯ��"�ՒZ�N����4�	�V���l(ی�z2[�kcB(,�I(�۞�_00y2�Ǆ�NՐNX�������Ýd0�����j'9�d�mI*��!�"�,QyH��4E�)�>e�K�a�0�&V�"��J��x�#,�}]�[b�ہ�׺}c��SbI&�%��'+E�d�=����KK��b�8x]Y��<3oĚ�c�=z!�G4��L����׉��)UF������3w��zti��"�F`ݩ�s��r=���J0s�b*�=y�S����IH����9ޟ<�S<��(����V�}|�����p� �����&��˨
&����3�����p��읉�ML�8�F�̡�
���^&�{N���8!ǮE��"<�-��b����,[(�I`v	AK:� �r��n|���*������f��l2�􊺜!|V��`K�|gi���yr��2���~��$��p��-_���&�H���/���\��h����`G��nv����q���@Vx�L���C�sͫ�*�$$�1�gU1���1�����z�}c���u�RR?�'��Ul7<�t���J�ۤ5]�1��u��Lk�A��C���x�����Y"����M��*ue��."o��3��.��{L�Oۉ'CL��t��Cc���
��6\��?*����	R�S�[����AE�&qu��o�>X���Иv⹓���ʮ��2�=�o��������      �   �  x��Wm�� �m"/�N��?�bL�13�٪4�Ѐ�1�O��g��x��!B}~�˳�8�"W�� ���q�8R@�ޱ�q:��w<i\@���]ǳ	�
�%�G O&��3��x����J$R�+@C!���=@�5ƟR�M�����v��Y�nPe@�"?�)�Ӕ`H��J=�c�!�0������V�1�F�V�j7������G	����3zԄ�Y����Lo� O���s��y�Ǻ\
��t
bt���?`(�ZA�G�����q
�ST	|L1Χ�W?Z�>������@����:�5�q] ��'3"����Ƌ�}��6߯��&6|L�?����L���kk������������#o�q��s��o���I~��.7�M��k�q����!�#��\�E랜;��a�N�z�E�'bjF�z[01O��i�K��7��{�L�3�^������]�<�wtO�5*�
@�����{h%��i������X^t5����d����T�ue=C�3���r���ڎ�����bJv]v�ک)^�5/y��s�/����[\9�e�oނ�:�j4ٕ����2SH6XZ�.ѽh1y���Jô+h����>X��W9�}��}vԜ����L��	t}O_�/AR��<&��q;I����>Bk�����(����~T/���m�� e��!     