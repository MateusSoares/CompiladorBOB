
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftVIRGrightATRIBMENOSCOMPATRIBCOMPDIVCOMPMULTCOMPrightCONDDOISPleftOULOGleftELOGleftOUleftEleftIGUALDIFERleftMENORMENORIGUALMAIORIGUALMAIORleftDESLESQDESLDIRleftMAISMENOSleftMULTDIVMODrightINCREMENDECREMNAOCOMPLEMleftABREPARFECHAPARABRECOLFECHACOLPONTEIROABRECOL ABRECV ABREPAR ATRIB ATRIBCOMP BREAK CLASS COMPLEM COND CONTINUE DECREM DEF DESLDIR DESLESQ DIFER DIV DIVCOMP DO DOISP E ELOG ELSE ERRO FECHACOL FECHACV FECHAPAR FLOAT FOR FOREACH IDENT IF IGUAL IN INCREMEN INT MAIOR MAIORIGUAL MAIS MENOR MENORIGUAL MENOS MENOSCOMP MOD MULT MULTCOMP NAO NEW NIL NUMBER OPESCOPO OU OULOG PONTEIRO PONTOV RETURN STATIC STRING VAR VIRG WHILEPrograma : ListaDefinicoesListaDefinicoes : ListaDefinicoes Definicao\n                       | empty  Definicao : DefinicaoClasse\n                  | DefinicaoFuncao DefinicaoClasse : CLASS IDENT ClasseBaseOpcional ABRECV ListaMembros FECHACV ClasseBaseOpcional : DOISP IDENT\n                           | empty ListaMembros : ListaMembros DefinicaoMembro\n                    | empty DefinicaoMembro : ModificadorOpcional VAR ListaVariaveis PONTOV\n                       | ModificadorOpcional DEF IDENT ABREPAR ListaArgsFormaisOpcional FECHAPAR PONTOV ModificadorOpcional : STATIC\n                           | empty ListaVariaveis : ListaVariaveis VIRG Variavel\n                      | Variavel Variavel : IDENT\n                | IDENT ABRECOL NUMBER FECHACOL ListaArgsFormaisOpcional : ListaArgsFormais\n                                | empty ListaArgsFormais : ListaArgsFormais VIRG IDENT\n                        | IDENT DefinicaoFuncao : DEF ClasseEnvolucroOpcional IDENT ABREPAR ListaParametrosOpcionais FECHAPAR BlocoClasseEnvolucroOpcional : IDENT OPESCOPO\n                               | empty ListaParametrosOpcionais : ListaArgsFormaisOpcional ListaTemporariosOpcionaisListaTemporariosOpcionais : PONTOV ListaArgsFormais\n                                 | empty Bloco : ABRECV ListaComandos FECHACVListaComandos : ListaComandos Comando\n                     | empty Comando : IF ABREPAR ExpOpc FECHAPAR Comando ELSE Comando\n               | IF ABREPAR ExpOpc FECHAPAR Comando\n               | WHILE ABREPAR ExpOpc FECHAPAR Comando\n               | DO Comando WHILE ABREPAR ExpOpc FECHAPAR PONTOV\n               | FOR ABREPAR ExpOpc PONTOV ExpOpc PONTOV ExpOpc FECHAPAR Comando\n               | FOREACH IDENT IN IDENT Comando\n               | BREAK PONTOV\n               | CONTINUE PONTOV\n               | RETURN ExpOpc PONTOV\n               | ExpOpc PONTOV\n               | Bloco ExpOpc : Exp\n              | empty Exp : Exp VIRG Exp\n           | EsqVal ATRIB Exp\n           | EsqVal ATRIBCOMP Exp\n           | EsqVal MENOSCOMP Exp\n           | EsqVal MULTCOMP Exp\n           | EsqVal DIVCOMP Exp\n           | Exp COND Exp DOISP Exp\n           | Exp OULOG Exp\n           | Exp ELOG Exp\n           | Exp OU Exp\n           | Exp E Exp\n           | Exp DESLESQ Exp\n           | Exp DESLDIR Exp\n           | Exp IGUAL Exp\n           | Exp DIFER Exp\n           | Exp MAIORIGUAL Exp\n           | Exp MENORIGUAL Exp\n           | Exp MAIOR Exp\n           | Exp MENOR Exp\n           | Exp MAIS Exp\n           | Exp MENOS Exp\n           | Exp MULT Exp\n           | Exp DIV Exp\n           | Exp MOD Exp\n           | DECREM EsqVal\n           | INCREMEN EsqVal\n           | EsqVal DECREM\n           | EsqVal INCREMEN\n           | NAO Exp\n           | COMPLEM Exp\n           | NEW IDENT ABREPAR ArgumentosOpcionais FECHAPAR\n           | IDENT ABREPAR ArgumentosOpcionais FECHAPAR\n           | Exp PONTEIRO IDENT ABREPAR ArgumentosOpcionais FECHAPAR\n           | IDENT\n           | IDENT ABRECOL Exp FECHACOL\n           | NUMBER\n           | STRING\n           | NIL ArgumentosOpcionais : Argumentos\n                           | empty Argumentos : Argumentos VIRG Exp\n                  | Exp EsqVal : IDENT\n              | IDENT ABRECOL Exp FECHACOL empty :'
    
_lr_action_items = {'CLASS':([0,2,3,4,5,6,28,40,54,],[-89,7,-3,-2,-4,-5,-6,-23,-29,]),'DEF':([0,2,3,4,5,6,18,21,22,28,29,30,31,32,40,50,54,165,],[-89,8,-3,-2,-4,-5,-89,-89,-10,-6,-9,39,-13,-14,-23,-11,-29,-12,]),'$end':([0,1,2,3,4,5,6,28,40,54,],[-89,0,-1,-3,-2,-4,-5,-6,-23,-29,]),'IDENT':([7,8,10,12,14,17,20,35,37,38,39,41,48,49,51,53,54,55,59,61,65,66,70,71,72,73,74,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,131,137,163,164,166,167,168,169,170,172,174,175,178,179,182,188,190,192,193,195,196,],[9,11,16,-25,19,-24,23,23,43,46,47,-89,62,-31,46,23,-29,-30,62,86,62,-42,120,120,62,62,124,62,-41,62,62,62,62,-38,-39,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,157,62,62,62,62,62,170,-40,62,62,62,62,62,62,62,62,62,62,-33,-34,-37,62,62,-32,-35,62,-36,]),'DOISP':([9,62,75,76,77,117,118,119,120,121,122,123,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,184,186,187,191,],[14,-78,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,-45,174,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-76,-79,-51,-88,-75,-77,]),'ABRECV':([9,13,15,19,33,41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,18,-8,-7,41,-89,41,-31,-29,-30,41,-42,-41,-38,-39,-40,41,41,41,-33,-34,-37,41,-32,-35,41,-36,]),'OPESCOPO':([11,],[17,]),'ABREPAR':([16,47,56,58,60,62,124,129,157,],[20,53,81,83,85,87,164,168,175,]),'FECHACV':([18,21,22,29,41,48,49,50,54,55,66,82,89,90,137,165,178,179,182,192,193,196,],[-89,28,-10,-9,-89,54,-31,-11,-29,-30,-42,-41,-38,-39,-40,-12,-33,-34,-37,-32,-35,-36,]),'STATIC':([18,21,22,29,50,165,],[-89,31,-10,-9,-11,-12,]),'VAR':([18,21,22,29,30,31,32,50,165,],[-89,-89,-10,-9,38,-13,-14,-11,-12,]),'PONTOV':([20,23,25,26,27,41,43,44,45,46,48,49,54,55,57,59,62,63,64,65,66,67,68,75,76,77,78,82,85,89,90,91,117,118,119,120,121,122,123,125,126,130,137,138,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,166,167,169,170,171,173,178,179,181,182,184,186,187,188,189,191,192,193,195,196,],[-89,-22,35,-19,-20,-89,-21,50,-16,-17,-89,-31,-29,-30,82,-89,-78,89,90,-89,-42,-43,-44,-80,-81,-82,-15,-41,-89,-38,-39,137,-71,-72,-69,-87,-70,-73,-74,-18,165,169,-40,-45,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-89,-89,-89,-89,-76,-79,-33,-34,190,-37,-51,-88,-75,-89,193,-77,-32,-35,-89,-36,]),'FECHAPAR':([20,23,24,25,26,27,34,36,42,43,53,62,67,68,75,76,77,80,81,83,87,117,118,119,120,121,122,123,127,128,132,133,134,135,138,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,164,168,171,173,175,177,180,183,184,185,186,187,190,191,194,],[-89,-22,33,-89,-19,-20,-26,-28,-27,-21,-89,-78,-43,-44,-80,-81,-82,126,-89,-89,-89,-71,-72,-69,-87,-70,-73,-74,166,167,171,-83,-84,-86,-45,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-89,-89,-76,-79,-89,187,189,-85,-51,191,-88,-75,-89,-77,195,]),'VIRG':([23,26,42,43,44,45,46,62,67,75,76,77,78,117,118,119,120,121,122,123,125,133,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-22,37,37,-21,51,-16,-17,-78,92,-80,-81,-82,-15,-71,-72,-69,-87,-70,-73,-74,-18,172,92,92,-45,92,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-76,-79,92,-85,-51,-88,-75,-77,]),'IF':([41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,56,-31,-29,-30,56,-42,-41,-38,-39,-40,56,56,56,-33,-34,-37,56,-32,-35,56,-36,]),'WHILE':([41,48,49,54,55,59,66,82,84,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,58,-31,-29,-30,58,-42,-41,129,-38,-39,-40,58,58,58,-33,-34,-37,58,-32,-35,58,-36,]),'DO':([41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,59,-31,-29,-30,59,-42,-41,-38,-39,-40,59,59,59,-33,-34,-37,59,-32,-35,59,-36,]),'FOR':([41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,60,-31,-29,-30,60,-42,-41,-38,-39,-40,60,60,60,-33,-34,-37,60,-32,-35,60,-36,]),'FOREACH':([41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,61,-31,-29,-30,61,-42,-41,-38,-39,-40,61,61,61,-33,-34,-37,61,-32,-35,61,-36,]),'BREAK':([41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,63,-31,-29,-30,63,-42,-41,-38,-39,-40,63,63,63,-33,-34,-37,63,-32,-35,63,-36,]),'CONTINUE':([41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,64,-31,-29,-30,64,-42,-41,-38,-39,-40,64,64,64,-33,-34,-37,64,-32,-35,64,-36,]),'RETURN':([41,48,49,54,55,59,66,82,89,90,137,166,167,170,178,179,182,188,192,193,195,196,],[-89,65,-31,-29,-30,65,-42,-41,-38,-39,-40,65,65,65,-33,-34,-37,65,-32,-35,65,-36,]),'DECREM':([41,48,49,54,55,59,62,65,66,69,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,173,174,175,178,179,182,188,190,192,193,195,196,],[-89,70,-31,-29,-30,70,-87,70,-42,117,70,70,70,-41,70,70,70,70,-38,-39,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-40,70,70,70,70,70,70,70,70,-88,70,70,-33,-34,-37,70,70,-32,-35,70,-36,]),'INCREMEN':([41,48,49,54,55,59,62,65,66,69,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,173,174,175,178,179,182,188,190,192,193,195,196,],[-89,71,-31,-29,-30,71,-87,71,-42,118,71,71,71,-41,71,71,71,71,-38,-39,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-40,71,71,71,71,71,71,71,71,-88,71,71,-33,-34,-37,71,71,-32,-35,71,-36,]),'NAO':([41,48,49,54,55,59,65,66,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,174,175,178,179,182,188,190,192,193,195,196,],[-89,72,-31,-29,-30,72,72,-42,72,72,72,-41,72,72,72,72,-38,-39,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-40,72,72,72,72,72,72,72,72,72,72,-33,-34,-37,72,72,-32,-35,72,-36,]),'COMPLEM':([41,48,49,54,55,59,65,66,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,174,175,178,179,182,188,190,192,193,195,196,],[-89,73,-31,-29,-30,73,73,-42,73,73,73,-41,73,73,73,73,-38,-39,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,-40,73,73,73,73,73,73,73,73,73,73,-33,-34,-37,73,73,-32,-35,73,-36,]),'NEW':([41,48,49,54,55,59,65,66,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,174,175,178,179,182,188,190,192,193,195,196,],[-89,74,-31,-29,-30,74,74,-42,74,74,74,-41,74,74,74,74,-38,-39,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,-40,74,74,74,74,74,74,74,74,74,74,-33,-34,-37,74,74,-32,-35,74,-36,]),'NUMBER':([41,48,49,52,54,55,59,65,66,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,174,175,178,179,182,188,190,192,193,195,196,],[-89,75,-31,79,-29,-30,75,75,-42,75,75,75,-41,75,75,75,75,-38,-39,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,-40,75,75,75,75,75,75,75,75,75,75,-33,-34,-37,75,75,-32,-35,75,-36,]),'STRING':([41,48,49,54,55,59,65,66,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,174,175,178,179,182,188,190,192,193,195,196,],[-89,76,-31,-29,-30,76,76,-42,76,76,76,-41,76,76,76,76,-38,-39,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,-40,76,76,76,76,76,76,76,76,76,76,-33,-34,-37,76,76,-32,-35,76,-36,]),'NIL':([41,48,49,54,55,59,65,66,72,73,81,82,83,85,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,137,163,164,166,167,168,169,170,172,174,175,178,179,182,188,190,192,193,195,196,],[-89,77,-31,-29,-30,77,77,-42,77,77,77,-41,77,77,77,77,-38,-39,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,-40,77,77,77,77,77,77,77,77,77,77,-33,-34,-37,77,77,-32,-35,77,-36,]),'ABRECOL':([46,62,120,],[52,88,163,]),'ELSE':([54,66,82,89,90,137,178,179,182,192,193,196,],[-29,-42,-41,-38,-39,-40,-33,-34,-37,-32,-35,-36,]),'COND':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,93,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,93,93,93,93,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,93,93,93,93,93,-76,-79,93,93,93,-88,-75,-77,]),'OULOG':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,94,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,94,94,94,94,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,94,94,94,94,94,-76,-79,94,94,94,-88,-75,-77,]),'ELOG':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,95,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,95,95,95,95,95,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,95,95,95,95,95,-76,-79,95,95,95,-88,-75,-77,]),'OU':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,96,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,96,96,96,96,96,96,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,96,96,96,96,96,-76,-79,96,96,96,-88,-75,-77,]),'E':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,97,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,97,97,97,97,97,97,97,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,97,97,97,97,97,-76,-79,97,97,97,-88,-75,-77,]),'DESLESQ':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,98,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,98,98,98,98,98,98,98,98,-56,-57,98,98,98,98,98,98,-64,-65,-66,-67,-68,98,98,98,98,98,-76,-79,98,98,98,-88,-75,-77,]),'DESLDIR':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,99,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,99,99,99,99,99,99,99,99,-56,-57,99,99,99,99,99,99,-64,-65,-66,-67,-68,99,99,99,99,99,-76,-79,99,99,99,-88,-75,-77,]),'IGUAL':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,100,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,100,100,100,100,100,100,100,100,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,100,100,100,100,100,-76,-79,100,100,100,-88,-75,-77,]),'DIFER':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,101,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,101,101,101,101,101,101,101,101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,101,101,101,101,101,-76,-79,101,101,101,-88,-75,-77,]),'MAIORIGUAL':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,102,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,102,102,102,102,102,102,102,102,-56,-57,102,102,-60,-61,-62,-63,-64,-65,-66,-67,-68,102,102,102,102,102,-76,-79,102,102,102,-88,-75,-77,]),'MENORIGUAL':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,103,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,103,103,103,103,103,103,103,103,-56,-57,103,103,-60,-61,-62,-63,-64,-65,-66,-67,-68,103,103,103,103,103,-76,-79,103,103,103,-88,-75,-77,]),'MAIOR':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,104,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,104,104,104,104,104,104,104,104,-56,-57,104,104,-60,-61,-62,-63,-64,-65,-66,-67,-68,104,104,104,104,104,-76,-79,104,104,104,-88,-75,-77,]),'MENOR':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,105,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,105,105,105,105,105,105,105,105,-56,-57,105,105,-60,-61,-62,-63,-64,-65,-66,-67,-68,105,105,105,105,105,-76,-79,105,105,105,-88,-75,-77,]),'MAIS':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,106,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,-64,-65,-66,-67,-68,106,106,106,106,106,-76,-79,106,106,106,-88,-75,-77,]),'MENOS':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,107,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,-64,-65,-66,-67,-68,107,107,107,107,107,-76,-79,107,107,107,-88,-75,-77,]),'MULT':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,108,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,-66,-67,-68,108,108,108,108,108,-76,-79,108,108,108,-88,-75,-77,]),'DIV':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,109,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,-66,-67,-68,109,109,109,109,109,-76,-79,109,109,109,-88,-75,-77,]),'MOD':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,110,-80,-81,-82,-71,-72,-69,-87,-70,-73,-74,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,-66,-67,-68,110,110,110,110,110,-76,-79,110,110,110,-88,-75,-77,]),'PONTEIRO':([62,67,75,76,77,117,118,119,120,121,122,123,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,183,184,186,187,191,],[-78,111,-80,-81,-82,-71,-72,-69,-87,-70,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,-76,-79,111,111,111,-88,-75,-77,]),'FECHACOL':([62,75,76,77,79,117,118,119,120,121,122,123,136,138,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,171,173,176,184,186,187,191,],[-78,-80,-81,-82,125,-71,-72,-69,-87,-70,-73,-74,173,-45,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-46,-47,-48,-49,-50,-76,-79,186,-51,-88,-75,-77,]),'ATRIB':([62,69,173,],[-87,112,-88,]),'ATRIBCOMP':([62,69,173,],[-87,113,-88,]),'MENOSCOMP':([62,69,173,],[-87,114,-88,]),'MULTCOMP':([62,69,173,],[-87,115,-88,]),'DIVCOMP':([62,69,173,],[-87,116,-88,]),'IN':([86,],[131,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'ListaDefinicoes':([0,],[2,]),'empty':([0,8,9,18,20,21,25,41,48,53,59,65,81,83,85,87,164,166,167,168,169,170,175,188,190,195,],[3,12,15,22,27,32,36,49,68,27,68,68,68,68,68,134,134,68,68,68,68,68,134,68,68,68,]),'Definicao':([2,],[4,]),'DefinicaoClasse':([2,],[5,]),'DefinicaoFuncao':([2,],[6,]),'ClasseEnvolucroOpcional':([8,],[10,]),'ClasseBaseOpcional':([9,],[13,]),'ListaMembros':([18,],[21,]),'ListaParametrosOpcionais':([20,],[24,]),'ListaArgsFormaisOpcional':([20,53,],[25,80,]),'ListaArgsFormais':([20,35,53,],[26,42,26,]),'DefinicaoMembro':([21,],[29,]),'ModificadorOpcional':([21,],[30,]),'ListaTemporariosOpcionais':([25,],[34,]),'Bloco':([33,48,59,166,167,170,188,195,],[40,66,66,66,66,66,66,66,]),'ListaVariaveis':([38,],[44,]),'Variavel':([38,51,],[45,78,]),'ListaComandos':([41,],[48,]),'Comando':([48,59,166,167,170,188,195,],[55,84,178,179,182,192,196,]),'ExpOpc':([48,59,65,81,83,85,166,167,168,169,170,188,190,195,],[57,57,91,127,128,130,57,57,180,181,57,57,194,57,]),'Exp':([48,59,65,72,73,81,83,85,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,163,164,166,167,168,169,170,172,174,175,188,190,195,],[67,67,67,122,123,67,67,67,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,162,176,135,67,67,67,67,67,183,184,135,67,67,67,]),'EsqVal':([48,59,65,70,71,72,73,81,83,85,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,163,164,166,167,168,169,170,172,174,175,188,190,195,],[69,69,69,119,121,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'ArgumentosOpcionais':([87,164,175,],[132,177,185,]),'Argumentos':([87,164,175,],[133,133,133,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> ListaDefinicoes','Programa',1,'p_Programa','sintaticoBob.py',32),
  ('ListaDefinicoes -> ListaDefinicoes Definicao','ListaDefinicoes',2,'p_ListaDefinicoes','sintaticoBob.py',37),
  ('ListaDefinicoes -> empty','ListaDefinicoes',1,'p_ListaDefinicoes','sintaticoBob.py',38),
  ('Definicao -> DefinicaoClasse','Definicao',1,'p_Definicao','sintaticoBob.py',43),
  ('Definicao -> DefinicaoFuncao','Definicao',1,'p_Definicao','sintaticoBob.py',44),
  ('DefinicaoClasse -> CLASS IDENT ClasseBaseOpcional ABRECV ListaMembros FECHACV','DefinicaoClasse',6,'p_DefinicaoClasse','sintaticoBob.py',49),
  ('ClasseBaseOpcional -> DOISP IDENT','ClasseBaseOpcional',2,'p_ClasseBaseOpcional','sintaticoBob.py',54),
  ('ClasseBaseOpcional -> empty','ClasseBaseOpcional',1,'p_ClasseBaseOpcional','sintaticoBob.py',55),
  ('ListaMembros -> ListaMembros DefinicaoMembro','ListaMembros',2,'p_ListaMembros','sintaticoBob.py',60),
  ('ListaMembros -> empty','ListaMembros',1,'p_ListaMembros','sintaticoBob.py',61),
  ('DefinicaoMembro -> ModificadorOpcional VAR ListaVariaveis PONTOV','DefinicaoMembro',4,'p_DefinicaoMembro','sintaticoBob.py',66),
  ('DefinicaoMembro -> ModificadorOpcional DEF IDENT ABREPAR ListaArgsFormaisOpcional FECHAPAR PONTOV','DefinicaoMembro',7,'p_DefinicaoMembro','sintaticoBob.py',67),
  ('ModificadorOpcional -> STATIC','ModificadorOpcional',1,'p_ModificadorOpcional','sintaticoBob.py',72),
  ('ModificadorOpcional -> empty','ModificadorOpcional',1,'p_ModificadorOpcional','sintaticoBob.py',73),
  ('ListaVariaveis -> ListaVariaveis VIRG Variavel','ListaVariaveis',3,'p_ListaVariaveis','sintaticoBob.py',78),
  ('ListaVariaveis -> Variavel','ListaVariaveis',1,'p_ListaVariaveis','sintaticoBob.py',79),
  ('Variavel -> IDENT','Variavel',1,'p_Variavel','sintaticoBob.py',83),
  ('Variavel -> IDENT ABRECOL NUMBER FECHACOL','Variavel',4,'p_Variavel','sintaticoBob.py',84),
  ('ListaArgsFormaisOpcional -> ListaArgsFormais','ListaArgsFormaisOpcional',1,'p_ListaArgsFormaisOpcional','sintaticoBob.py',88),
  ('ListaArgsFormaisOpcional -> empty','ListaArgsFormaisOpcional',1,'p_ListaArgsFormaisOpcional','sintaticoBob.py',89),
  ('ListaArgsFormais -> ListaArgsFormais VIRG IDENT','ListaArgsFormais',3,'p_ListaArgsFormais','sintaticoBob.py',94),
  ('ListaArgsFormais -> IDENT','ListaArgsFormais',1,'p_ListaArgsFormais','sintaticoBob.py',95),
  ('DefinicaoFuncao -> DEF ClasseEnvolucroOpcional IDENT ABREPAR ListaParametrosOpcionais FECHAPAR Bloco','DefinicaoFuncao',7,'p_DefinicaoFuncao','sintaticoBob.py',100),
  ('ClasseEnvolucroOpcional -> IDENT OPESCOPO','ClasseEnvolucroOpcional',2,'p_ClasseEnvolucroOpcional','sintaticoBob.py',105),
  ('ClasseEnvolucroOpcional -> empty','ClasseEnvolucroOpcional',1,'p_ClasseEnvolucroOpcional','sintaticoBob.py',106),
  ('ListaParametrosOpcionais -> ListaArgsFormaisOpcional ListaTemporariosOpcionais','ListaParametrosOpcionais',2,'p_ListaParametrosOpcionais','sintaticoBob.py',111),
  ('ListaTemporariosOpcionais -> PONTOV ListaArgsFormais','ListaTemporariosOpcionais',2,'p_ListaTemporariosOpcionais','sintaticoBob.py',116),
  ('ListaTemporariosOpcionais -> empty','ListaTemporariosOpcionais',1,'p_ListaTemporariosOpcionais','sintaticoBob.py',117),
  ('Bloco -> ABRECV ListaComandos FECHACV','Bloco',3,'p_Bloco','sintaticoBob.py',122),
  ('ListaComandos -> ListaComandos Comando','ListaComandos',2,'p_ListaComandos','sintaticoBob.py',127),
  ('ListaComandos -> empty','ListaComandos',1,'p_ListaComandos','sintaticoBob.py',128),
  ('Comando -> IF ABREPAR ExpOpc FECHAPAR Comando ELSE Comando','Comando',7,'p_Comando','sintaticoBob.py',133),
  ('Comando -> IF ABREPAR ExpOpc FECHAPAR Comando','Comando',5,'p_Comando','sintaticoBob.py',134),
  ('Comando -> WHILE ABREPAR ExpOpc FECHAPAR Comando','Comando',5,'p_Comando','sintaticoBob.py',135),
  ('Comando -> DO Comando WHILE ABREPAR ExpOpc FECHAPAR PONTOV','Comando',7,'p_Comando','sintaticoBob.py',136),
  ('Comando -> FOR ABREPAR ExpOpc PONTOV ExpOpc PONTOV ExpOpc FECHAPAR Comando','Comando',9,'p_Comando','sintaticoBob.py',137),
  ('Comando -> FOREACH IDENT IN IDENT Comando','Comando',5,'p_Comando','sintaticoBob.py',138),
  ('Comando -> BREAK PONTOV','Comando',2,'p_Comando','sintaticoBob.py',139),
  ('Comando -> CONTINUE PONTOV','Comando',2,'p_Comando','sintaticoBob.py',140),
  ('Comando -> RETURN ExpOpc PONTOV','Comando',3,'p_Comando','sintaticoBob.py',141),
  ('Comando -> ExpOpc PONTOV','Comando',2,'p_Comando','sintaticoBob.py',142),
  ('Comando -> Bloco','Comando',1,'p_Comando','sintaticoBob.py',143),
  ('ExpOpc -> Exp','ExpOpc',1,'p_ExpOpc','sintaticoBob.py',148),
  ('ExpOpc -> empty','ExpOpc',1,'p_ExpOpc','sintaticoBob.py',149),
  ('Exp -> Exp VIRG Exp','Exp',3,'p_Exp','sintaticoBob.py',154),
  ('Exp -> EsqVal ATRIB Exp','Exp',3,'p_Exp','sintaticoBob.py',155),
  ('Exp -> EsqVal ATRIBCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',156),
  ('Exp -> EsqVal MENOSCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',157),
  ('Exp -> EsqVal MULTCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',158),
  ('Exp -> EsqVal DIVCOMP Exp','Exp',3,'p_Exp','sintaticoBob.py',159),
  ('Exp -> Exp COND Exp DOISP Exp','Exp',5,'p_Exp','sintaticoBob.py',160),
  ('Exp -> Exp OULOG Exp','Exp',3,'p_Exp','sintaticoBob.py',161),
  ('Exp -> Exp ELOG Exp','Exp',3,'p_Exp','sintaticoBob.py',162),
  ('Exp -> Exp OU Exp','Exp',3,'p_Exp','sintaticoBob.py',163),
  ('Exp -> Exp E Exp','Exp',3,'p_Exp','sintaticoBob.py',164),
  ('Exp -> Exp DESLESQ Exp','Exp',3,'p_Exp','sintaticoBob.py',165),
  ('Exp -> Exp DESLDIR Exp','Exp',3,'p_Exp','sintaticoBob.py',166),
  ('Exp -> Exp IGUAL Exp','Exp',3,'p_Exp','sintaticoBob.py',167),
  ('Exp -> Exp DIFER Exp','Exp',3,'p_Exp','sintaticoBob.py',168),
  ('Exp -> Exp MAIORIGUAL Exp','Exp',3,'p_Exp','sintaticoBob.py',169),
  ('Exp -> Exp MENORIGUAL Exp','Exp',3,'p_Exp','sintaticoBob.py',170),
  ('Exp -> Exp MAIOR Exp','Exp',3,'p_Exp','sintaticoBob.py',171),
  ('Exp -> Exp MENOR Exp','Exp',3,'p_Exp','sintaticoBob.py',172),
  ('Exp -> Exp MAIS Exp','Exp',3,'p_Exp','sintaticoBob.py',173),
  ('Exp -> Exp MENOS Exp','Exp',3,'p_Exp','sintaticoBob.py',174),
  ('Exp -> Exp MULT Exp','Exp',3,'p_Exp','sintaticoBob.py',175),
  ('Exp -> Exp DIV Exp','Exp',3,'p_Exp','sintaticoBob.py',176),
  ('Exp -> Exp MOD Exp','Exp',3,'p_Exp','sintaticoBob.py',177),
  ('Exp -> DECREM EsqVal','Exp',2,'p_Exp','sintaticoBob.py',178),
  ('Exp -> INCREMEN EsqVal','Exp',2,'p_Exp','sintaticoBob.py',179),
  ('Exp -> EsqVal DECREM','Exp',2,'p_Exp','sintaticoBob.py',180),
  ('Exp -> EsqVal INCREMEN','Exp',2,'p_Exp','sintaticoBob.py',181),
  ('Exp -> NAO Exp','Exp',2,'p_Exp','sintaticoBob.py',182),
  ('Exp -> COMPLEM Exp','Exp',2,'p_Exp','sintaticoBob.py',183),
  ('Exp -> NEW IDENT ABREPAR ArgumentosOpcionais FECHAPAR','Exp',5,'p_Exp','sintaticoBob.py',184),
  ('Exp -> IDENT ABREPAR ArgumentosOpcionais FECHAPAR','Exp',4,'p_Exp','sintaticoBob.py',185),
  ('Exp -> Exp PONTEIRO IDENT ABREPAR ArgumentosOpcionais FECHAPAR','Exp',6,'p_Exp','sintaticoBob.py',186),
  ('Exp -> IDENT','Exp',1,'p_Exp','sintaticoBob.py',187),
  ('Exp -> IDENT ABRECOL Exp FECHACOL','Exp',4,'p_Exp','sintaticoBob.py',188),
  ('Exp -> NUMBER','Exp',1,'p_Exp','sintaticoBob.py',189),
  ('Exp -> STRING','Exp',1,'p_Exp','sintaticoBob.py',190),
  ('Exp -> NIL','Exp',1,'p_Exp','sintaticoBob.py',191),
  ('ArgumentosOpcionais -> Argumentos','ArgumentosOpcionais',1,'p_ArgumentosOpcionais','sintaticoBob.py',196),
  ('ArgumentosOpcionais -> empty','ArgumentosOpcionais',1,'p_ArgumentosOpcionais','sintaticoBob.py',197),
  ('Argumentos -> Argumentos VIRG Exp','Argumentos',3,'p_Argumentos','sintaticoBob.py',202),
  ('Argumentos -> Exp','Argumentos',1,'p_Argumentos','sintaticoBob.py',203),
  ('EsqVal -> IDENT','EsqVal',1,'p_EsqVal','sintaticoBob.py',208),
  ('EsqVal -> IDENT ABRECOL Exp FECHACOL','EsqVal',4,'p_EsqVal','sintaticoBob.py',209),
  ('empty -> <empty>','empty',0,'p_empty','sintaticoBob.py',214),
]
