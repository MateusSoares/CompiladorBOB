
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightNAOleftEOUnonassocIGUALDIFERMAIORMENORMAIORIGUALMENORIGUALleftMULTDIVMODleftMAISMENOSABRECOL ABRECV ABREPAR ATRIB ATRIBCOMP BREAK CLASS COMPLEM COND CONTINUE DECREM DESLDIR DESLESQ DIFER DIV DIVCOMP DO DOISP E ELOG ELSE ERRO FECHACOL FECHACV FECHAPAR FOR FOREACH IDENT IF IGUAL IN INCREMEN MAIOR MAIORIGUAL MAIS MENOR MENORIGUAL MENOS MENOSCOMP MOD MULT MULTCOMP NAO NEW NIL NUMBER OPESCOPO OU OULOG PONTEIRO PONTOV RETURN STATIC STRING VIRG WHILEPrograma : ListaDefinicoesListaDefinicoes : ListaDefinicoes Definicao\n                       | empty  Definicao : DefinicaoClasse\n                  | DefinicaoFuncao DefinicaoClasse : CLASS IDENT ClasseBaseOpcional ABRECV ListaMembros FECHACV ClasseBaseOpcional : DOISP IDENT\n                           | empty ListaMembros : ListaMembros DefinicaoMembro\n                    | empty DefinicaoMembro : ModificadorOpcional ListaVariaveis PONTOV\n                       | ModificadorOpcional IDENT ABREPAR ListaArgsFormaisOpcional FECHAPAR PONTOV ModificadorOpcional : STATIC\n                           | empty ListaVariaveis : ListaVariaveis VIRG Variavel\n                      | Variavel Variavel : IDENT\n                | IDENT ABRECOL NUMBER FECHACOL ListaArgsFormaisOpcional : ListaArgsFormais\n                                | empty ListaArgsFormais : ListaArgsFormais VIRG IDENT\n                        | IDENT DefinicaoFuncao : ClasseEnvolucroOpcional IDENT ABREPAR ListaParametrosOpcionais FECHAPAR BlocoClasseEnvolucroOpcional : IDENT OPESCOPO\n                               | empty ListaParametrosOpcionais : ListaArgsFormaisOpcional ListaTemporariosOpcionaisListaTemporariosOpcionais : PONTOV ListaArgsFormais\n                                 | empty Bloco : ABRECV ListaComandos FECHACVListaComandos : ListaComandos Comando\n                     | empty Comando : IF ABREPAR ExpOpc FECHAPAR Comando ELSE Comando\n               | IF ABREPAR ExpOpc FECHAPAR Comando\n               | WHILE ABREPAR ExpOpc FECHAPAR Comando\n               | DO Comando WHILE ABREPAR ExpOpc FECHAPAR PONTOV\n               | FOR ABREPAR ExpOpc PONTOV ExpOpc PONTOV ExpOpc FECHAPAR Comando\n               | FOREACH IDENT IN IDENT Comando\n               | BREAK PONTOV\n               | CONTINUE PONTOV\n               | RETURN ExpOpc PONTOV\n               | ExpOpc PONTOV\n               | Bloco ExpOpc : Exp\n              | empty Exp : Exp VIRG Exp\n           | EsqVal ATRIB Exp\n           | EsqVal ATRIBCOMP Exp\n           | EsqVal MENOSCOMP Exp\n           | EsqVal MULTCOMP Exp\n           | EsqVal DIVCOMP Exp\n           | Exp COND Exp DOISP Exp\n           | Exp OULOG Exp\n           | Exp ELOG Exp\n           | Exp OU Exp\n           | Exp E Exp\n           | Exp DESLESQ Exp\n           | Exp DESLDIR Exp\n           | Exp IGUAL Exp\n           | Exp DIFER Exp\n           | Exp MAIORIGUAL Exp\n           | Exp MENORIGUAL Exp\n           | Exp MAIOR Exp\n           | Exp MENOR Exp\n           | Exp MAIS Exp\n           | Exp MENOS Exp\n           | Exp MULT Exp\n           | Exp DIV Exp\n           | Exp MOD Exp\n           | DECREM EsqVal\n           | INCREMEN EsqVal\n           | EsqVal DECREM\n           | EsqVal INCREMEN\n           | NAO Exp\n           | COMPLEM Exp\n           | NEW IDENT ABREPAR ArgumentosOpcionais FECHAPAR\n           | IDENT ABREPAR ArgumentosOpcionais FECHAPAR\n           | Exp PONTEIRO ABREPAR ArgumentosOpcionais FECHAPAR\n           | IDENT\n           | IDENT ABRECOL Exp FECHACOL\n           | NUMBER\n           | STRING\n           | NIL ArgumentosOpcionais : Argumentos\n                           | empty Argumentos : Argumentos VIRG Exp\n                  | Exp EsqVal : IDENT\n              | IDENT ABRECOL Exp FECHACOL empty :'
    
_lr_action_items = {'CLASS':([0,2,3,4,5,6,32,37,50,],[-89,7,-3,-2,-4,-5,-6,-23,-29,]),'IDENT':([0,2,3,4,5,6,7,9,10,12,15,17,18,25,26,29,31,32,33,34,35,36,37,38,44,45,46,47,48,50,51,55,57,61,62,66,67,68,69,70,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,128,134,154,160,161,162,163,164,165,166,167,169,171,175,176,179,185,187,188,189,191,192,],[-89,8,-3,-2,-4,-5,11,13,-25,-24,19,20,-89,-89,-10,20,40,-6,-9,42,-13,-14,-23,-89,58,-31,-11,75,20,-29,-30,58,83,58,-42,117,117,58,58,121,58,-41,58,58,58,58,-38,-39,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,167,-40,58,58,58,-12,58,58,58,58,58,58,58,-33,-34,-37,58,58,-32,-35,58,-36,]),'$end':([0,1,2,3,4,5,6,32,37,50,],[-89,0,-1,-3,-2,-4,-5,-6,-23,-29,]),'OPESCOPO':([8,],[12,]),'DOISP':([11,58,71,72,73,114,115,116,117,118,119,120,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,181,182,183,184,],[15,-78,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,-45,171,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-76,-79,-51,-77,-88,-75,]),'ABRECV':([11,14,16,19,27,38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,18,-8,-7,38,-89,38,-31,-29,-30,38,-42,-41,-38,-39,-40,38,38,38,-33,-34,-37,38,-32,-35,38,-36,]),'ABREPAR':([13,42,52,54,56,58,108,121,126,],[17,48,78,80,82,84,154,161,165,]),'PONTOV':([17,20,22,23,24,38,40,41,42,43,44,45,50,51,53,55,58,59,60,61,62,63,64,71,72,73,74,75,79,82,86,87,88,114,115,116,117,118,119,120,122,123,127,134,135,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,163,164,166,167,168,170,175,176,178,179,181,182,183,184,185,186,188,189,191,192,],[-89,-22,29,-19,-20,-89,-21,46,-17,-16,-89,-31,-29,-30,79,-89,-78,86,87,-89,-42,-43,-44,-80,-81,-82,-15,-17,-41,-89,-38,-39,134,-71,-72,-69,-87,-70,-73,-74,162,-18,166,-40,-45,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-89,-89,-89,-89,-76,-79,-33,-34,187,-37,-51,-77,-88,-75,-89,189,-32,-35,-89,-36,]),'FECHAPAR':([17,20,21,22,23,24,28,30,39,40,48,58,63,64,71,72,73,76,78,80,84,114,115,116,117,118,119,120,124,125,129,130,131,132,135,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,161,165,168,170,172,174,177,180,181,182,183,184,187,190,],[-89,-22,27,-89,-19,-20,-26,-28,-27,-21,-89,-78,-43,-44,-80,-81,-82,122,-89,-89,-89,-71,-72,-69,-87,-70,-73,-74,163,164,168,-83,-84,-86,-45,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-89,-46,-47,-48,-49,-50,-89,-89,-76,-79,182,184,186,-85,-51,-77,-88,-75,-89,191,]),'FECHACV':([18,25,26,33,38,44,45,46,50,51,62,79,86,87,134,162,175,176,179,188,189,192,],[-89,32,-10,-9,-89,50,-31,-11,-29,-30,-42,-41,-38,-39,-40,-12,-33,-34,-37,-32,-35,-36,]),'STATIC':([18,25,26,33,46,162,],[-89,35,-10,-9,-11,-12,]),'VIRG':([20,23,39,40,41,42,43,58,63,71,72,73,74,75,114,115,116,117,118,119,120,123,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-22,31,31,-21,47,-17,-16,-78,89,-80,-81,-82,-15,-17,-71,-72,-69,-87,-70,-73,89,-18,169,89,89,89,89,89,89,-54,-55,89,89,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,89,89,89,89,89,-76,-79,89,89,89,-77,-88,-75,]),'IF':([38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,52,-31,-29,-30,52,-42,-41,-38,-39,-40,52,52,52,-33,-34,-37,52,-32,-35,52,-36,]),'WHILE':([38,44,45,50,51,55,62,79,81,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,54,-31,-29,-30,54,-42,-41,126,-38,-39,-40,54,54,54,-33,-34,-37,54,-32,-35,54,-36,]),'DO':([38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,55,-31,-29,-30,55,-42,-41,-38,-39,-40,55,55,55,-33,-34,-37,55,-32,-35,55,-36,]),'FOR':([38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,56,-31,-29,-30,56,-42,-41,-38,-39,-40,56,56,56,-33,-34,-37,56,-32,-35,56,-36,]),'FOREACH':([38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,57,-31,-29,-30,57,-42,-41,-38,-39,-40,57,57,57,-33,-34,-37,57,-32,-35,57,-36,]),'BREAK':([38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,59,-31,-29,-30,59,-42,-41,-38,-39,-40,59,59,59,-33,-34,-37,59,-32,-35,59,-36,]),'CONTINUE':([38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,60,-31,-29,-30,60,-42,-41,-38,-39,-40,60,60,60,-33,-34,-37,60,-32,-35,60,-36,]),'RETURN':([38,44,45,50,51,55,62,79,86,87,134,163,164,167,175,176,179,185,188,189,191,192,],[-89,61,-31,-29,-30,61,-42,-41,-38,-39,-40,61,61,61,-33,-34,-37,61,-32,-35,61,-36,]),'DECREM':([38,44,45,50,51,55,58,61,62,65,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,170,171,175,176,179,185,187,188,189,191,192,],[-89,66,-31,-29,-30,66,-87,66,-42,114,66,66,66,-41,66,66,66,66,-38,-39,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-40,66,66,66,66,66,66,66,66,66,-88,66,-33,-34,-37,66,66,-32,-35,66,-36,]),'INCREMEN':([38,44,45,50,51,55,58,61,62,65,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,170,171,175,176,179,185,187,188,189,191,192,],[-89,67,-31,-29,-30,67,-87,67,-42,115,67,67,67,-41,67,67,67,67,-38,-39,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-40,67,67,67,67,67,67,67,67,67,-88,67,-33,-34,-37,67,67,-32,-35,67,-36,]),'NAO':([38,44,45,50,51,55,61,62,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,171,175,176,179,185,187,188,189,191,192,],[-89,68,-31,-29,-30,68,68,-42,68,68,68,-41,68,68,68,68,-38,-39,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,-40,68,68,68,68,68,68,68,68,68,68,-33,-34,-37,68,68,-32,-35,68,-36,]),'COMPLEM':([38,44,45,50,51,55,61,62,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,171,175,176,179,185,187,188,189,191,192,],[-89,69,-31,-29,-30,69,69,-42,69,69,69,-41,69,69,69,69,-38,-39,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,-40,69,69,69,69,69,69,69,69,69,69,-33,-34,-37,69,69,-32,-35,69,-36,]),'NEW':([38,44,45,50,51,55,61,62,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,171,175,176,179,185,187,188,189,191,192,],[-89,70,-31,-29,-30,70,70,-42,70,70,70,-41,70,70,70,70,-38,-39,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-40,70,70,70,70,70,70,70,70,70,70,-33,-34,-37,70,70,-32,-35,70,-36,]),'NUMBER':([38,44,45,49,50,51,55,61,62,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,171,175,176,179,185,187,188,189,191,192,],[-89,71,-31,77,-29,-30,71,71,-42,71,71,71,-41,71,71,71,71,-38,-39,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-40,71,71,71,71,71,71,71,71,71,71,-33,-34,-37,71,71,-32,-35,71,-36,]),'STRING':([38,44,45,50,51,55,61,62,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,171,175,176,179,185,187,188,189,191,192,],[-89,72,-31,-29,-30,72,72,-42,72,72,72,-41,72,72,72,72,-38,-39,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-40,72,72,72,72,72,72,72,72,72,72,-33,-34,-37,72,72,-32,-35,72,-36,]),'NIL':([38,44,45,50,51,55,61,62,68,69,78,79,80,82,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,134,154,160,161,163,164,165,166,167,169,171,175,176,179,185,187,188,189,191,192,],[-89,73,-31,-29,-30,73,73,-42,73,73,73,-41,73,73,73,73,-38,-39,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,-40,73,73,73,73,73,73,73,73,73,73,-33,-34,-37,73,73,-32,-35,73,-36,]),'ABRECOL':([42,58,75,117,],[49,85,49,160,]),'ELSE':([50,62,79,86,87,134,175,176,179,188,189,192,],[-29,-42,-41,-38,-39,-40,185,-34,-37,-32,-35,-36,]),'COND':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,90,-80,-81,-82,-71,-72,-69,-87,-70,-73,90,90,90,90,90,90,90,-54,-55,90,90,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,90,90,90,90,90,-76,-79,90,90,90,-77,-88,-75,]),'OULOG':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,91,-80,-81,-82,-71,-72,-69,-87,-70,-73,91,91,91,91,91,91,91,-54,-55,91,91,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,91,91,91,91,91,-76,-79,91,91,91,-77,-88,-75,]),'ELOG':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,92,-80,-81,-82,-71,-72,-69,-87,-70,-73,92,92,92,92,92,92,92,-54,-55,92,92,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,92,92,92,92,92,-76,-79,92,92,92,-77,-88,-75,]),'OU':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,93,-80,-81,-82,-71,-72,-69,-87,-70,93,93,93,93,93,93,93,93,-54,-55,93,93,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,93,93,93,93,93,-76,-79,93,93,93,-77,-88,-75,]),'E':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,94,-80,-81,-82,-71,-72,-69,-87,-70,94,94,94,94,94,94,94,94,-54,-55,94,94,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,94,94,94,94,94,-76,-79,94,94,94,-77,-88,-75,]),'DESLESQ':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,95,-80,-81,-82,-71,-72,-69,-87,-70,-73,95,95,95,95,95,95,95,-54,-55,95,95,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,95,95,95,95,95,-76,-79,95,95,95,-77,-88,-75,]),'DESLDIR':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,96,-80,-81,-82,-71,-72,-69,-87,-70,-73,96,96,96,96,96,96,96,-54,-55,96,96,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,96,96,96,96,96,-76,-79,96,96,96,-77,-88,-75,]),'IGUAL':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,97,-80,-81,-82,-71,-72,-69,-87,-70,97,97,97,97,97,97,97,97,97,97,97,97,None,None,None,None,None,None,-64,-65,-66,-67,-68,97,97,97,97,97,-76,-79,97,97,97,-77,-88,-75,]),'DIFER':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,98,-80,-81,-82,-71,-72,-69,-87,-70,98,98,98,98,98,98,98,98,98,98,98,98,None,None,None,None,None,None,-64,-65,-66,-67,-68,98,98,98,98,98,-76,-79,98,98,98,-77,-88,-75,]),'MAIORIGUAL':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,99,-80,-81,-82,-71,-72,-69,-87,-70,99,99,99,99,99,99,99,99,99,99,99,99,None,None,None,None,None,None,-64,-65,-66,-67,-68,99,99,99,99,99,-76,-79,99,99,99,-77,-88,-75,]),'MENORIGUAL':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,100,-80,-81,-82,-71,-72,-69,-87,-70,100,100,100,100,100,100,100,100,100,100,100,100,None,None,None,None,None,None,-64,-65,-66,-67,-68,100,100,100,100,100,-76,-79,100,100,100,-77,-88,-75,]),'MAIOR':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,101,-80,-81,-82,-71,-72,-69,-87,-70,101,101,101,101,101,101,101,101,101,101,101,101,None,None,None,None,None,None,-64,-65,-66,-67,-68,101,101,101,101,101,-76,-79,101,101,101,-77,-88,-75,]),'MENOR':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,102,-80,-81,-82,-71,-72,-69,-87,-70,102,102,102,102,102,102,102,102,102,102,102,102,None,None,None,None,None,None,-64,-65,-66,-67,-68,102,102,102,102,102,-76,-79,102,102,102,-77,-88,-75,]),'MAIS':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,103,-80,-81,-82,-71,-72,-69,-87,-70,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,-64,-65,103,103,103,103,103,103,103,103,-76,-79,103,103,103,-77,-88,-75,]),'MENOS':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,104,-80,-81,-82,-71,-72,-69,-87,-70,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,-64,-65,104,104,104,104,104,104,104,104,-76,-79,104,104,104,-77,-88,-75,]),'MULT':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,105,-80,-81,-82,-71,-72,-69,-87,-70,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,-64,-65,-66,-67,-68,105,105,105,105,105,-76,-79,105,105,105,-77,-88,-75,]),'DIV':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,106,-80,-81,-82,-71,-72,-69,-87,-70,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,-64,-65,-66,-67,-68,106,106,106,106,106,-76,-79,106,106,106,-77,-88,-75,]),'MOD':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,107,-80,-81,-82,-71,-72,-69,-87,-70,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,-64,-65,-66,-67,-68,107,107,107,107,107,-76,-79,107,107,107,-77,-88,-75,]),'PONTEIRO':([58,63,71,72,73,114,115,116,117,118,119,120,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,180,181,182,183,184,],[-78,108,-80,-81,-82,-71,-72,-69,-87,-70,-73,108,108,108,108,108,108,108,-54,-55,108,108,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,108,108,108,108,108,-76,-79,108,108,108,-77,-88,-75,]),'FECHACOL':([58,71,72,73,77,114,115,116,117,118,119,120,133,135,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,168,170,173,181,182,183,184,],[-78,-80,-81,-82,123,-71,-72,-69,-87,-70,-73,-74,170,-45,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-76,-79,183,-51,-77,-88,-75,]),'ATRIB':([58,65,170,],[-87,109,-88,]),'ATRIBCOMP':([58,65,170,],[-87,110,-88,]),'MENOSCOMP':([58,65,170,],[-87,111,-88,]),'MULTCOMP':([58,65,170,],[-87,112,-88,]),'DIVCOMP':([58,65,170,],[-87,113,-88,]),'IN':([83,],[128,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'ListaDefinicoes':([0,],[2,]),'empty':([0,2,11,17,18,22,25,38,44,48,55,61,78,80,82,84,154,161,163,164,165,166,167,185,187,191,],[3,10,16,24,26,30,36,45,64,24,64,64,64,64,64,131,131,131,64,64,64,64,64,64,64,64,]),'Definicao':([2,],[4,]),'DefinicaoClasse':([2,],[5,]),'DefinicaoFuncao':([2,],[6,]),'ClasseEnvolucroOpcional':([2,],[9,]),'ClasseBaseOpcional':([11,],[14,]),'ListaParametrosOpcionais':([17,],[21,]),'ListaArgsFormaisOpcional':([17,48,],[22,76,]),'ListaArgsFormais':([17,29,48,],[23,39,23,]),'ListaMembros':([18,],[25,]),'ListaTemporariosOpcionais':([22,],[28,]),'DefinicaoMembro':([25,],[33,]),'ModificadorOpcional':([25,],[34,]),'Bloco':([27,44,55,163,164,167,185,191,],[37,62,62,62,62,62,62,62,]),'ListaVariaveis':([34,],[41,]),'Variavel':([34,47,],[43,74,]),'ListaComandos':([38,],[44,]),'Comando':([44,55,163,164,167,185,191,],[51,81,175,176,179,188,192,]),'ExpOpc':([44,55,61,78,80,82,163,164,165,166,167,185,187,191,],[53,53,88,124,125,127,53,53,177,178,53,53,190,53,]),'Exp':([44,55,61,68,69,78,80,82,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,154,160,161,163,164,165,166,167,169,171,185,187,191,],[63,63,63,119,120,63,63,63,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,155,156,157,158,159,132,173,132,63,63,63,63,63,180,181,63,63,63,]),'EsqVal':([44,55,61,66,67,68,69,78,80,82,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,154,160,161,163,164,165,166,167,169,171,185,187,191,],[65,65,65,116,118,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'ArgumentosOpcionais':([84,154,161,],[129,172,174,]),'Argumentos':([84,154,161,],[130,130,130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> ListaDefinicoes','Programa',1,'p_Programa','sintaticoBob.py',23),
  ('ListaDefinicoes -> ListaDefinicoes Definicao','ListaDefinicoes',2,'p_ListaDefinicoes','sintaticoBob.py',28),
  ('ListaDefinicoes -> empty','ListaDefinicoes',1,'p_ListaDefinicoes','sintaticoBob.py',29),
  ('Definicao -> DefinicaoClasse','Definicao',1,'p_Definicao','sintaticoBob.py',34),
  ('Definicao -> DefinicaoFuncao','Definicao',1,'p_Definicao','sintaticoBob.py',35),
  ('DefinicaoClasse -> CLASS IDENT ClasseBaseOpcional ABRECV ListaMembros FECHACV','DefinicaoClasse',6,'p_DefinicaoClasse','sintaticoBob.py',40),
  ('ClasseBaseOpcional -> DOISP IDENT','ClasseBaseOpcional',2,'p_ClasseBaseOpcional','sintaticoBob.py',45),
  ('ClasseBaseOpcional -> empty','ClasseBaseOpcional',1,'p_ClasseBaseOpcional','sintaticoBob.py',46),
  ('ListaMembros -> ListaMembros DefinicaoMembro','ListaMembros',2,'p_ListaMembros','sintaticoBob.py',51),
  ('ListaMembros -> empty','ListaMembros',1,'p_ListaMembros','sintaticoBob.py',52),
  ('DefinicaoMembro -> ModificadorOpcional ListaVariaveis PONTOV','DefinicaoMembro',3,'p_DefinicaoMembro','sintaticoBob.py',57),
  ('DefinicaoMembro -> ModificadorOpcional IDENT ABREPAR ListaArgsFormaisOpcional FECHAPAR PONTOV','DefinicaoMembro',6,'p_DefinicaoMembro','sintaticoBob.py',58),
  ('ModificadorOpcional -> STATIC','ModificadorOpcional',1,'p_ModificadorOpcional','sintaticoBob.py',63),
  ('ModificadorOpcional -> empty','ModificadorOpcional',1,'p_ModificadorOpcional','sintaticoBob.py',64),
  ('ListaVariaveis -> ListaVariaveis VIRG Variavel','ListaVariaveis',3,'p_ListaVariaveis','sintaticoBob.py',69),
  ('ListaVariaveis -> Variavel','ListaVariaveis',1,'p_ListaVariaveis','sintaticoBob.py',70),
  ('Variavel -> IDENT','Variavel',1,'p_Variavel','sintaticoBob.py',74),
  ('Variavel -> IDENT ABRECOL NUMBER FECHACOL','Variavel',4,'p_Variavel','sintaticoBob.py',75),
  ('ListaArgsFormaisOpcional -> ListaArgsFormais','ListaArgsFormaisOpcional',1,'p_ListaArgsFormaisOpcional','sintaticoBob.py',79),
  ('ListaArgsFormaisOpcional -> empty','ListaArgsFormaisOpcional',1,'p_ListaArgsFormaisOpcional','sintaticoBob.py',80),
  ('ListaArgsFormais -> ListaArgsFormais VIRG IDENT','ListaArgsFormais',3,'p_ListaArgsFormais','sintaticoBob.py',85),
  ('ListaArgsFormais -> IDENT','ListaArgsFormais',1,'p_ListaArgsFormais','sintaticoBob.py',86),
  ('DefinicaoFuncao -> ClasseEnvolucroOpcional IDENT ABREPAR ListaParametrosOpcionais FECHAPAR Bloco','DefinicaoFuncao',6,'p_DefinicaoFuncao','sintaticoBob.py',91),
  ('ClasseEnvolucroOpcional -> IDENT OPESCOPO','ClasseEnvolucroOpcional',2,'p_ClasseEnvolucroOpcional','sintaticoBob.py',96),
  ('ClasseEnvolucroOpcional -> empty','ClasseEnvolucroOpcional',1,'p_ClasseEnvolucroOpcional','sintaticoBob.py',97),
  ('ListaParametrosOpcionais -> ListaArgsFormaisOpcional ListaTemporariosOpcionais','ListaParametrosOpcionais',2,'p_ListaParametrosOpcionais','sintaticoBob.py',102),
  ('ListaTemporariosOpcionais -> PONTOV ListaArgsFormais','ListaTemporariosOpcionais',2,'p_ListaTemporariosOpcionais','sintaticoBob.py',107),
  ('ListaTemporariosOpcionais -> empty','ListaTemporariosOpcionais',1,'p_ListaTemporariosOpcionais','sintaticoBob.py',108),
  ('Bloco -> ABRECV ListaComandos FECHACV','Bloco',3,'p_Bloco','sintaticoBob.py',113),
  ('ListaComandos -> ListaComandos Comando','ListaComandos',2,'p_ListaComandos','sintaticoBob.py',118),
  ('ListaComandos -> empty','ListaComandos',1,'p_ListaComandos','sintaticoBob.py',119),
  ('Comando -> IF ABREPAR ExpOpc FECHAPAR Comando ELSE Comando','Comando',7,'p_Comando','sintaticoBob.py',124),
  ('Comando -> IF ABREPAR ExpOpc FECHAPAR Comando','Comando',5,'p_Comando','sintaticoBob.py',125),
  ('Comando -> WHILE ABREPAR ExpOpc FECHAPAR Comando','Comando',5,'p_Comando','sintaticoBob.py',126),
  ('Comando -> DO Comando WHILE ABREPAR ExpOpc FECHAPAR PONTOV','Comando',7,'p_Comando','sintaticoBob.py',127),
  ('Comando -> FOR ABREPAR ExpOpc PONTOV ExpOpc PONTOV ExpOpc FECHAPAR Comando','Comando',9,'p_Comando','sintaticoBob.py',128),
  ('Comando -> FOREACH IDENT IN IDENT Comando','Comando',5,'p_Comando','sintaticoBob.py',129),
  ('Comando -> BREAK PONTOV','Comando',2,'p_Comando','sintaticoBob.py',130),
  ('Comando -> CONTINUE PONTOV','Comando',2,'p_Comando','sintaticoBob.py',131),
  ('Comando -> RETURN ExpOpc PONTOV','Comando',3,'p_Comando','sintaticoBob.py',132),
  ('Comando -> ExpOpc PONTOV','Comando',2,'p_Comando','sintaticoBob.py',133),
  ('Comando -> Bloco','Comando',1,'p_Comando','sintaticoBob.py',134),
  ('ExpOpc -> Exp','ExpOpc',1,'p_ExpOpc','sintaticoBob.py',139),
  ('ExpOpc -> empty','ExpOpc',1,'p_ExpOpc','sintaticoBob.py',140),
  ('Exp -> Exp VIRG Exp','Exp',3,'p_Exp','sintaticoBob.py',145),
  ('Exp -> EsqVal ATRIB Exp','Exp',3,'p_Exp','sintaticoBob.py',146),
  ('Exp -> EsqVal ATRIBCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',147),
  ('Exp -> EsqVal MENOSCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',148),
  ('Exp -> EsqVal MULTCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',149),
  ('Exp -> EsqVal DIVCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',150),
  ('Exp -> Exp COND Exp DOISP Exp','Exp',5,'p_Exp','sintaticoBob.py',151),
  ('Exp -> Exp OULOG Exp','Exp',3,'p_Exp','sintaticoBob.py',152),
  ('Exp -> Exp ELOG Exp','Exp',3,'p_Exp','sintaticoBob.py',153),
  ('Exp -> Exp OU Exp','Exp',3,'p_Exp','sintaticoBob.py',154),
  ('Exp -> Exp E Exp','Exp',3,'p_Exp','sintaticoBob.py',155),
  ('Exp -> Exp DESLESQ Exp','Exp',3,'p_Exp','sintaticoBob.py',156),
  ('Exp -> Exp DESLDIR Exp','Exp',3,'p_Exp','sintaticoBob.py',157),
  ('Exp -> Exp IGUAL Exp','Exp',3,'p_Exp','sintaticoBob.py',158),
  ('Exp -> Exp DIFER Exp','Exp',3,'p_Exp','sintaticoBob.py',159),
  ('Exp -> Exp MAIORIGUAL Exp','Exp',3,'p_Exp','sintaticoBob.py',160),
  ('Exp -> Exp MENORIGUAL Exp','Exp',3,'p_Exp','sintaticoBob.py',161),
  ('Exp -> Exp MAIOR Exp','Exp',3,'p_Exp','sintaticoBob.py',162),
  ('Exp -> Exp MENOR Exp','Exp',3,'p_Exp','sintaticoBob.py',163),
  ('Exp -> Exp MAIS Exp','Exp',3,'p_Exp','sintaticoBob.py',164),
  ('Exp -> Exp MENOS Exp','Exp',3,'p_Exp','sintaticoBob.py',165),
  ('Exp -> Exp MULT Exp','Exp',3,'p_Exp','sintaticoBob.py',166),
  ('Exp -> Exp DIV Exp','Exp',3,'p_Exp','sintaticoBob.py',167),
  ('Exp -> Exp MOD Exp','Exp',3,'p_Exp','sintaticoBob.py',168),
  ('Exp -> DECREM EsqVal','Exp',2,'p_Exp','sintaticoBob.py',169),
  ('Exp -> INCREMEN EsqVal','Exp',2,'p_Exp','sintaticoBob.py',170),
  ('Exp -> EsqVal DECREM','Exp',2,'p_Exp','sintaticoBob.py',171),
  ('Exp -> EsqVal INCREMEN','Exp',2,'p_Exp','sintaticoBob.py',172),
  ('Exp -> NAO Exp','Exp',2,'p_Exp','sintaticoBob.py',173),
  ('Exp -> COMPLEM Exp','Exp',2,'p_Exp','sintaticoBob.py',174),
  ('Exp -> NEW IDENT ABREPAR ArgumentosOpcionais FECHAPAR','Exp',5,'p_Exp','sintaticoBob.py',175),
  ('Exp -> IDENT ABREPAR ArgumentosOpcionais FECHAPAR','Exp',4,'p_Exp','sintaticoBob.py',176),
  ('Exp -> Exp PONTEIRO ABREPAR ArgumentosOpcionais FECHAPAR','Exp',5,'p_Exp','sintaticoBob.py',177),
  ('Exp -> IDENT','Exp',1,'p_Exp','sintaticoBob.py',178),
  ('Exp -> IDENT ABRECOL Exp FECHACOL','Exp',4,'p_Exp','sintaticoBob.py',179),
  ('Exp -> NUMBER','Exp',1,'p_Exp','sintaticoBob.py',180),
  ('Exp -> STRING','Exp',1,'p_Exp','sintaticoBob.py',181),
  ('Exp -> NIL','Exp',1,'p_Exp','sintaticoBob.py',182),
  ('ArgumentosOpcionais -> Argumentos','ArgumentosOpcionais',1,'p_ArgumentosOpcionais','sintaticoBob.py',187),
  ('ArgumentosOpcionais -> empty','ArgumentosOpcionais',1,'p_ArgumentosOpcionais','sintaticoBob.py',188),
  ('Argumentos -> Argumentos VIRG Exp','Argumentos',3,'p_Argumentos','sintaticoBob.py',193),
  ('Argumentos -> Exp','Argumentos',1,'p_Argumentos','sintaticoBob.py',194),
  ('EsqVal -> IDENT','EsqVal',1,'p_EsqVal','sintaticoBob.py',199),
  ('EsqVal -> IDENT ABRECOL Exp FECHACOL','EsqVal',4,'p_EsqVal','sintaticoBob.py',200),
  ('empty -> <empty>','empty',0,'p_empty','sintaticoBob.py',205),
]