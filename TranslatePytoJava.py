from PytoJavaListener import PytoJavaListener
from PytoJavaParser import *

class TranslatePytoJava(PytoJavaListener):
    def __init__(self):
        self.inside_main = False  # To track if we're inside the main method.

    # Enter a parse tree produced by PytoJavaParser#program.
    def enterProgram(self, ctx: PytoJavaParser.ProgramContext):
        print("public class Main {\n")

    # Exit a parse tree produced by PytoJavaParser#program.
    def exitProgram(self, ctx: PytoJavaParser.ProgramContext):
        # Close the Java class after all methods.
        print("\n}")

    # Enter a parse tree produced by PytoJavaParser#functionDef.
    def enterFunctionDef(self, ctx: PytoJavaParser.FunctionDefContext):
        func_name = ctx.ID().getText()  # Get function name.
        if func_name == "main":  # Special handling for `main` function.
            self.inside_main = True
            print("    public static void main(String[] args) {")
        else:
            print(f"    public static int {func_name}(", end="")
            if ctx.parameters():
                params = []
                for param in ctx.parameters().ID():
                    params.append(f"int {param.getText()}")
                print(", ".join(params), end="")
            print(") {")  # Start function block.

    # Exit a parse tree produced by PytoJavaParser#functionDef.
    def exitFunctionDef(self, ctx: PytoJavaParser.FunctionDefContext):
        print("    }")  # Close the function block.
        if self.inside_main:
            self.inside_main = False  # Reset main function tracking.

    # Enter a parse tree produced by PytoJavaParser#parameters.
    def enterParameters(self, ctx: PytoJavaParser.ParametersContext):
        pass  # Parameters are processed in enterFunctionDef.

    # Exit a parse tree produced by PytoJavaParser#parameters.
    def exitParameters(self, ctx: PytoJavaParser.ParametersContext):
        pass

    # Enter a parse tree produced by PytoJavaParser#statements.
    def enterStatements(self, ctx: PytoJavaParser.StatementsContext):
        pass

    # Exit a parse tree produced by PytoJavaParser#statements.
    def exitStatements(self, ctx: PytoJavaParser.StatementsContext):
        pass

    # Enter a parse tree produced by PytoJavaParser#statement.
    def enterStatement(self, ctx: PytoJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by PytoJavaParser#statement.
    def exitStatement(self, ctx: PytoJavaParser.StatementContext):
        print(";")  # Ensure semicolon at the end of statements.

    # Enter a parse tree produced by PytoJavaParser#returnStmt.
    def enterReturnStmt(self, ctx: PytoJavaParser.ReturnStmtContext):
        return_expr = ctx.expression().getText()
        print(f"        return {return_expr}", end="")

    # Exit a parse tree produced by PytoJavaParser#returnStmt.
    def exitReturnStmt(self, ctx: PytoJavaParser.ReturnStmtContext):
        pass

    # Enter a parse tree produced by PytoJavaParser#printStmt.
    def enterPrintStmt(self, ctx: PytoJavaParser.PrintStmtContext):
        expr = ctx.expression().getText()
        print(f"        System.out.println({expr}", end="")

    # Exit a parse tree produced by PytoJavaParser#printStmt.
    def exitPrintStmt(self, ctx: PytoJavaParser.PrintStmtContext):
        pass

    # Enter a parse tree produced by PytoJavaParser#exprStmt.
    def enterExprStmt(self, ctx: PytoJavaParser.ExprStmtContext):
        if ctx.ASSIGN():
            var_name = ctx.ID().getText()
            value = ctx.expression().getText()
            print(f"        int {var_name} = {value}", end="")
        else:
            expr = ctx.expression().getText()
            print(f"        {expr}", end="")

    # Exit a parse tree produced by PytoJavaParser#exprStmt.
    def exitExprStmt(self, ctx: PytoJavaParser.ExprStmtContext):
        pass
