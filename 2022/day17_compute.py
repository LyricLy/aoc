changes = "4212320123421330013200132400021003342033001330013340133001304013030132221013013211121220032203032103201322013200122400030212130133020032202242133221330213211130321212212110133021321213340130421332013222123401222012301130421320012122130301304213040133400031013322123000203013222133221330002340133401332013042121301332213200133001301201322133020220012222033201214013020132201330012220132021321002320133001330013212123001322013340132011214213220133201330212120033221321213240121201334012211033221330003020113021332002300032001330200302130220032212322133201320003220020221332013300132201324210002132201330003302123201332212342033201303012302121201330213220133001230012211130301330012122122020304202320121301332013222133000230013240133001330012122123201320013322122221302212340132201330013222132001302213340133001324012132022201322013340022111214002340003001212212140013201124013042123021212213320132001330013320133201330013300112111334002000121101212012300133201334013200132001222010220122221334012300132121213012122122001332003340133201322013300013400222012122133421321213302132201232013322133400010113300103200232012120030301304012120133400032013340133000203012220130121334012122123201320010322130201330213032133001332213340130301332212301133001213003210121221302213300130300234010340132201324213300133021322211240133001321112140132201234213340133400220013322132220030013300122420221113240132221222013240133401222012320121201332013220133201332013222133001212212120130421330013040121201324212320130301321012320133201004212300112201332013202003221321113042121401334002220133001212012340121300322213340132401301113220023401030013022132400030212320123021212013320022400030013320132001222013040130300230212342121221210212240133"
start = "1234000340133221303003300022221222012142133000222200342132001322013022132021324213040021421332013322132221332213340020010302002220133001330013240003401324212242133021330012320133001334012300133000222002040130400201202200133001334213340132"
q, r = divmod(1000000000000-len(start), len(changes))
print(sum(int(x) for x in changes)*q+sum(int(x) for x in start)+sum(int(x) for x in changes[:r]))