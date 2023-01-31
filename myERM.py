digraph model_graph {
fontname="Roboto";
fontsize=8;
rankdir="TB";
splines=true;
node [fontname="Roboto", fontsize=8, shape="plaintext"];
edge [fontname="Roboto", fontsize=8];
django_contrib_admin_models_LogEntry [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    LogEntry
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>AutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><B>content_type</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>user</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">action_flag</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">PositiveSmallIntegerField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">action_time</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">change_message</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">object_id</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">object_repr</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_auth_models_AbstractUser [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    AbstractUser<BR/>&lt;<FONT FACE="Roboto"><I>AbstractBaseUser,PermissionsMixin</I></FONT>&gt;
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">date_joined</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">email</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">EmailField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">first_name</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">is_active</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">BooleanField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">is_staff</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">BooleanField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>is_superuser</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>BooleanField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_login</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>DateTimeField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">last_name</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>password</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>CharField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">username</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_auth_models_Permission [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Permission
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>AutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>content_type</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">codename</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">name</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_auth_models_Group [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Group
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>AutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">name</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_auth_models_User [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    User<BR/>&lt;<FONT FACE="Roboto"><I>AbstractUser</I></FONT>&gt;
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>AutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>date_joined</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>email</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>EmailField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>first_name</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>CharField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>is_active</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>BooleanField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>is_staff</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>BooleanField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>is_superuser</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>BooleanField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_login</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>DateTimeField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_name</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto"><I>CharField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>password</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>CharField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>username</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>CharField</I></FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_contenttypes_models_ContentType [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    ContentType
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>AutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">app_label</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">model</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_sessions_base_session_AbstractBaseSession [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    AbstractBaseSession
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">expire_date</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">session_data</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">TextField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_sessions_models_Session [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Session<BR/>&lt;<FONT FACE="Roboto"><I>AbstractBaseSession</I></FONT>&gt;
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I><B>session_key</B></I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I><B>CharField</B></I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>expire_date</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><I>session_data</I></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><I>TextField</I></FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
products_models_Tag [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Tag
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">name</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
products_models_Product [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Product
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">available</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">BooleanField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">brand</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">condition</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">dateOfUpload</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">DateField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">descriptionText</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">name</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">price</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">FloatField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
profiles_models_Profile [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Profile
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>user</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>OneToOneField (id)</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">account_number</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">address</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">created</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">updated</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
buyers_models_Buyer [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Buyer
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>user</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>OneToOneField (id)</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">address</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">buyerID</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">created</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">dateOfBirth</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">DateField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">updated</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
sellers_models_Seller [label=<
    <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
    <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
    <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
    Seller
    </B></FONT></TD></TR>
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>id</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto"><B>user</B></FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto"><B>OneToOneField (id)</B></FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">address</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">created</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT FACE="Roboto">dateOfBirth</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT FACE="Roboto">DateField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">sellerID</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
    </TD></TR>
  
  
  
    <TR><TD ALIGN="LEFT" BORDER="0">
    <FONT COLOR="#7B7B7B" FACE="Roboto">updated</FONT>
    </TD><TD ALIGN="LEFT">
    <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
    </TD></TR>
  
  
    </TABLE>
    >];
django_contrib_admin_models_LogEntry -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" user (logentry)"];
django_contrib_admin_models_LogEntry -> django_contrib_contenttypes_models_ContentType  [arrowhead=none, arrowtail=dot, dir=both, label=" content_type (logentry)"];
django_contrib_auth_base_user_AbstractBaseUser [label=<
  <TABLE BGCOLOR="white" BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="#1b563f">
  <FONT FACE="Roboto" POINT-SIZE="12" COLOR="white">AbstractBaseUser</FONT>
  </TD></TR>
  </TABLE>
  >];
django_contrib_auth_models_AbstractUser -> django_contrib_auth_base_user_AbstractBaseUser  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
django_contrib_auth_models_PermissionsMixin [label=<
  <TABLE BGCOLOR="white" BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="#1b563f">
  <FONT FACE="Roboto" POINT-SIZE="12" COLOR="white">PermissionsMixin</FONT>
  </TD></TR>
  </TABLE>
  >];
django_contrib_auth_models_AbstractUser -> django_contrib_auth_models_PermissionsMixin  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
django_contrib_auth_models_Permission -> django_contrib_contenttypes_models_ContentType  [arrowhead=none, arrowtail=dot, dir=both, label=" content_type (permission)"];
django_contrib_auth_models_Group -> django_contrib_auth_models_Permission  [arrowhead=dot, arrowtail=dot, dir=both, label=" permissions (group)"];
django_contrib_auth_models_User -> django_contrib_auth_models_Group  [arrowhead=dot, arrowtail=dot, dir=both, label=" groups (user)"];
django_contrib_auth_models_User -> django_contrib_auth_models_Permission  [arrowhead=dot, arrowtail=dot, dir=both, label=" user_permissions (user)"];
django_contrib_auth_models_User -> django_contrib_auth_models_AbstractUser  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
django_contrib_sessions_models_Session -> django_contrib_sessions_base_session_AbstractBaseSession  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
products_models_Product -> products_models_Tag  [arrowhead=dot, arrowtail=dot, dir=both, label=" tags (product)"];
profiles_models_Profile -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=none, dir=both, label=" user (profile)"];
buyers_models_Buyer -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=none, dir=both, label=" user (buyer)"];
sellers_models_Seller -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=none, dir=both, label=" user (seller)"];
"\n\n\n";
}
