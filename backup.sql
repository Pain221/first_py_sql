PGDMP                         {         	   komunalka    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16388 	   komunalka    DATABASE     }   CREATE DATABASE komunalka WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE komunalka;
                postgres    false            �            1259    16389    accruals    TABLE       CREATE TABLE public.accruals (
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
       public         heap    postgres    false            �            1259    16394 	   customers    TABLE       CREATE TABLE public.customers (
    number_ls integer NOT NULL,
    indications_date date NOT NULL,
    indications_hvs numeric,
    indications_gvs numeric,
    indications_ee_daytime numeric,
    number_of_residents integer,
    indications_ee_night numeric
);
    DROP TABLE public.customers;
       public         heap    postgres    false            �            1259    16399    users    TABLE     �   CREATE TABLE public.users (
    number_ls integer NOT NULL,
    password text NOT NULL,
    number_of_phone bigint NOT NULL,
    adress text NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false                       0    16389    accruals 
   TABLE DATA           �   COPY public.accruals (number_ls, accrual_date, accrual_hvs, accrual_gvs_heat_carrier, accrual_gvs_thermal_energy, accrual_total_gvs, accrual_ee, total_accrual) FROM stdin;
    public          postgres    false    214   �                 0    16394 	   customers 
   TABLE DATA           �   COPY public.customers (number_ls, indications_date, indications_hvs, indications_gvs, indications_ee_daytime, number_of_residents, indications_ee_night) FROM stdin;
    public          postgres    false    215   r                 0    16399    users 
   TABLE DATA           M   COPY public.users (number_ls, password, number_of_phone, adress) FROM stdin;
    public          postgres    false    216   �       m           2606    16405    accruals accruals_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.accruals
    ADD CONSTRAINT accruals_pkey PRIMARY KEY (number_ls, accrual_date);
 @   ALTER TABLE ONLY public.accruals DROP CONSTRAINT accruals_pkey;
       public            postgres    false    214    214            o           2606    16407    customers customers_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (number_ls, indications_date);
 B   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    215    215            q           2606    16409    users users_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (number_ls);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    216                v  x��Z[v�*���b�6qW0�_�H�@��cr}f!h���""��#�5����ӿ���v}�"���$(�b�ВK@Cߒo���[�L /����[ ]�����'/�����:�(!k?2�J�e��|�t^�*٭1m�#ˡ<Z$YW�`yl$wp3Jco���v�mQ�qi0�=H���)D��8Y�T� �- ���<�b��X��� �H�[��](��x~���v�h{s	�hqI0j%�Ɏgr�AU� =z1fCtp�m�¶�$��j4��!�_3T9�Y��#�0�0��&���{�^}o?�|�sJ8k_>#9�H�%Q0_S�I<�D��:�$pkZ��Kɰ�ZK��������,ܹ�������RHV���hz?0�J qa��ǥ�O�.�z�f�����,�F�-e���_�{0y��n7�;f;*�̑�b\9�M8 )3DK��#8��"�Y`W�w�ސ5l ��h�|?"	H�ի��k�%SZQ�D[D}S��4W��6�#��{�ԑ�`���ZE�S�2�L6�*����y �jZ�iT&�Q�ѳ����Z��)K����f|O?�Q����g�$C�v�����E�Kߤ�4�̺��23`�`I�Vd#�T�Wq��{
L��봚�G3#�8�!�¯�C�&�6�.z��B3azMZ/�p�Z!��z������(�B�$~�K�ا�5k�M�����qL��l�@p��)�_1W?c�}������1�t�t�n��ˠ\����P��8�ah��9�������k��S&� �!	��~c���~yZn�>�Z!Z7�>��K��J�&￴i���1��?�j�d78/	So�y�P��4������[���p����7���ۆ��N���2�#T8�*���[?)"pk��u��	��a�tZ̠��0ԛ[ V!�Vw4�S��^�Fn
�m�v�$K�]ԭWj[�8�&����:�`�|T48S�Vk�ܔ��)pa[$�qàΓ�^��&FpJ)�<�58����ΰ�!Ǒ�)dZ7a-�'n=1ى�7Ͼ��J�_��"�3��'| ,ʰ�"	��D�>qb�:��}�|��؊��?�gP�D_�g�g��0�ɇ:29ft2>6Y)�d|��A���v�/3\5���/餍ʾ_OP����R<PS�,k(IA-�Km��ۘt����f�����Z��U���ߵ���a�ϧP';�[Oz���T��_IQ|�-�V��&�SN����V5��K��k}�!�R_mx/��l2��o��IK;�*Q�j����t��G�)����aEl��z'���n��(hj�c�g�����+��r8�:z$��Ӊ���t[o�z�Va��k��dFtw�O��v�5�%�σ�_ϏzdD�� "�==�6ÕJ�D+��<���*� �P��������z�(Vlށ��}���%�{j���l�&���I��Ȱ7"�[��^n��Re`��/R�˙qPGG7�S�V���Q���߮���u���=Y_��U�W��t7����d�Ö��S���+������4Ѱ�&b��)&�$�R���&�)�>[��M�_�����|�ʛ%���.�{��Ӵ���(]io�S�Z����V�F�?��z lq8�.39f�+����H��Mw�ǖR�����GZ��%�IZ���4���DŎn��Ȼ:t����9�b�w����º���.a�U�>UO~G�/+^����a������I�տ͢��(ax�4�s��\�Dx:���������4�7��מ����M
_/�D�N��B8� �"�R���=�ǡ	;�4}�k��-�]���M���a�z�s}�������E�d����.��_�tD         T  x��X[��(���r{IH@&�#��G'�@b���s�r�����:�����?�:B<���_�����d�yA��)(����xD��q�q�`�u<�8��G�g���۵D[p|g�G��Y�����U0G �"���� �XU��"�qP�$6f���3w]�;}A��H�@o~#��*g���R��u4�j�k���I>酃��%�RͶF|�ɍ��Ǉ��ϨQ�~�w��AH��b|���:8 �G�}��|y�7��4c0	����	�� ף�O�^>�&�t�Ja
࣋���=C�Db����O����8���#�q
�|$8�I/����x���\x>M�����-���>���xkK�-��p�ƨn۝F����.PX�o~
M��<�;��[swr��<#����p����X?p59xw��SxA�'#�q���z���G$l�rZPBv�����KI?�u�^*n~��g�0Qoz�~G��sF�T��R���iZ���M�����X�f,o�MUsH<�FzVYoU){ȳaf=n�n�u����s6�=���݇����q��u�9/����ތ�rm�Wox�����.G�T6�瑙���ō�M s-j��N�\0�ڲr���:��N'����2�q�Y�F�K)�!��T��� Mzk?&��v�J�L�i�B%J���-2;׼�����=MH�ܗ���7
���V��%?���T��y�A�|�T/�9_s�,�8c��E���ǕE���e1����Ŵ���L,�1�xC{��G{���{���{�����A�*pa1m"̦�˽q��o����q0��x�?KٗN~;[�rm9�0T)��-�Wsi�s�h�UV5tÏ��vP��՛��]}a՟�[���e�ϒr�UE<�u��G�&o�5��n51�6&�;yp~�&�9%��4W _����R��tzl�&��pS+��;*�h].u����H���š�qP��>�J��"[5�9��_ո(c,[�Isn�v�N�����ނ�
v��������>xZ)������JKp[�^�N��U�q+3 ����W���~��s�         �  x�}�Kn!���9A���Ъ'見H����z��'51;������c�G��FDW�|�O����}�=\oǃqʷ�b ���&���Η�cV0kh�28tʁc0r�i��ݭ�5�VϺP+ �H<�*��0^�K�!D1<B*���<�aWU���=���5�u�y$�2V��Z�um�[�?���`:�;�'��㎻�]��8��<�8M�����3?��/C�R0v���\������$�Q����6ʻc� ��L�d��I�,�84Qд��'J�.�8DQ�=A,�`�%K<�ZEÕ�k�4�;M�5sY�T:�e3��aK�6s]��t��7S�����/�{�^��귡���P"��mT�i��Q�w.�4�|Bj݀�ڀ�¶�����G���Q)�B�m8     