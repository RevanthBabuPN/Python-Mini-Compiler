%{
    #include<stdio.h>
    #include<stdlib.h>
    #include <string.h>
	#include <stdarg.h>
	
	#define maxscopey 10000
	
	//because size of each scope(100) is 100 elements
	
	typedef struct symtabnode
	{
		char* name;
		int scope;
	}symtabnode;
	
	//will store all the elements and their scopes
	symtabnode symtab[maxscopey];
	int indexy=0;//first index to be filled in the symbol table

	void addtotable(char* name,int scope)
	{
		strcpy(symtab[indexy].name,name);
		symtab[indexy].scope=scope;
		++indexy;
	}

	static void searchele(char* name,int scope)
	{
		for(int i=0;i<indexy;++i)
		{
			if (strcmp(name,symtab[i].name)==0)
				return;
		}
		addtotable(name,scope);
	}

	void printTable()
	{
		printf("Name\t|Scope\t\n");
		for(int i=0;i<indexy;++i)
			printf("%s\t|%d\t",symtab[i].name,symtab[i].scope);
	}  
%}
%locations

%start start_karo
%union {struct symtabnode* data;};
%token T_NL T_IND T_DED T_EOF T_EQ T_Comma T_Del T_Pass T_Break T_Continue T_In
%token T_Print T_Import T_From T_Star T_LP T_RP T_Cln T_For T_While T_Or T_Range
%token T_And T_Not T_Lt T_Gt T_Lte T_Gte T_Deq T_Plus T_Minus T_Divide T_Mod T_DDiv
%token T_Power T_Ls T_Rs T_True T_False T_ID T_Integer T_Real T_String

%right T_Power
%right T_EQ
%left T_Plus T_Minus
%left T_Star T_Divide T_DDiv T_Mod
%left T_LP T_RP

%%

start_karo
	: T_NL start_karo
	| stmt T_NL start_karo
	| stmt T_NL
	| T_EOF {printTable();exit(0);}

term
	: math_term
	| T_String

math_term
	: T_ID {searchele($<data->name>1,$<data->scope>1);}
	| T_Real
	| T_Integer

stmt
	: simple_stmt

simple_stmt
	: base_stmt

base_stmt
	: pass_stmt
	| delete_stmt
	| import_stmt
	| cobr_stmt
	| assign_stmt
	| print_stmt
	| printable_stmt

pass_stmt
	: T_Pass

delete_stmt
	: T_Del T_ID

import_stmt
	: T_Import T_ID {searchele($<data->name>2,$<data->scope>2);}
	| import_from

import_from
	: T_From T_ID T_Import T_ID end_import_from

end_import_from
	: T_Comma T_ID end_import_from
	| %empty

cobr_stmt
	: T_Break
	| T_Continue

assign_stmt
	: T_ID T_EQ term {searchele($<data->name>1,$<data->scope>1);}
	| T_ID T_EQ printable_stmt {searchele($<data->name>1,$<data->scope>1);}

print_stmt
	: T_Print T_LP term T_RP
	| T_Print T_LP printable_stmt T_RP

printable_stmt
	: arith_stmt

arith_stmt
	: arith_stmt operator arith_stmt
	| T_LP arith_stmt T_RP
	| math_term
	| T_Minus math_term

operator
	: T_Plus
	| T_Minus
	| T_Star
	| T_Divide
	| T_DDiv
	| T_Mod

	
%%

