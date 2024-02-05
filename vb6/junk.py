
    # Enter a parse tree produced by VisualBasic6Parser#filecopyStmt.
    def enterFilecopyStmt(self, ctx:VisualBasic6Parser.FilecopyStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#filecopyStmt.
    def exitFilecopyStmt(self, ctx:VisualBasic6Parser.FilecopyStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#forEachStmt.
    def enterForEachStmt(self, ctx:VisualBasic6Parser.ForEachStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#forEachStmt.
    def exitForEachStmt(self, ctx:VisualBasic6Parser.ForEachStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#forNextStmt.
    def enterForNextStmt(self, ctx:VisualBasic6Parser.ForNextStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#forNextStmt.
    def exitForNextStmt(self, ctx:VisualBasic6Parser.ForNextStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)
 

    # Enter a parse tree produced by VisualBasic6Parser#asTypeClause.
    def enterAsTypeClause(self, ctx:VisualBasic6Parser.AsTypeClauseContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#asTypeClause.
    def exitAsTypeClause(self, ctx:VisualBasic6Parser.AsTypeClauseContext):
        self.depth -= 1
        info("exit", ctx, self.depth)

    # Enter a parse tree produced by VisualBasic6Parser#argDefaultValue.
    def enterArgDefaultValue(self, ctx:VisualBasic6Parser.ArgDefaultValueContext):
        self.depth += 1
        print("DEFAULT VALUE -'{0}' : {1}".format(self.tree.get_scope(),ctx.getText()))
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#argDefaultValue.
    def exitArgDefaultValue(self, ctx:VisualBasic6Parser.ArgDefaultValueContext):
        self.depth -= 1
        info("exit", ctx, self.depth)
    
    # Enter a parse tree produced by VisualBasic6Parser#ambiguousIdentifier.
    def enterAmbiguousIdentifier(self, ctx:VisualBasic6Parser.AmbiguousIdentifierContext):
        self.depth += 1
        #name=ctx.getText()

        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#ambiguousIdentifier.
    def exitAmbiguousIdentifier(self, ctx:VisualBasic6Parser.AmbiguousIdentifierContext):
        self.depth -= 1
        self.name=ctx.getText()
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#baseType.
    def enterBaseType(self, ctx:VisualBasic6Parser.BaseTypeContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#baseType.
    def exitBaseType(self, ctx:VisualBasic6Parser.BaseTypeContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#argList.
    def enterArgList(self, ctx:VisualBasic6Parser.ArgListContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#argList.
    def exitArgList(self, ctx:VisualBasic6Parser.ArgListContext):
        self.depth -= 1
        info("exit", ctx, self.depth)
s
    # Enter a parse tree produced by VisualBasic6Parser#certainIdentifier.
    def enterCertainIdentifier(self, ctx:VisualBasic6Parser.CertainIdentifierContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#certainIdentifier.
    def exitCertainIdentifier(self, ctx:VisualBasic6Parser.CertainIdentifierContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#comparisonOperator.
    def enterComparisonOperator(self, ctx:VisualBasic6Parser.ComparisonOperatorContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#comparisonOperator.
    def exitComparisonOperator(self, ctx:VisualBasic6Parser.ComparisonOperatorContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#complexType.
    def enterComplexType(self, ctx:VisualBasic6Parser.ComplexTypeContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#complexType.
    def exitComplexType(self, ctx:VisualBasic6Parser.ComplexTypeContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#fieldLength.
    def enterFieldLength(self, ctx:VisualBasic6Parser.FieldLengthContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#fieldLength.
    def exitFieldLength(self, ctx:VisualBasic6Parser.FieldLengthContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#letterrange.
    def enterLetterrange(self, ctx:VisualBasic6Parser.LetterrangeContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#letterrange.
    def exitLetterrange(self, ctx:VisualBasic6Parser.LetterrangeContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#lineLabel.
    def enterLineLabel(self, ctx:VisualBasic6Parser.LineLabelContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#lineLabel.
    def exitLineLabel(self, ctx:VisualBasic6Parser.LineLabelContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#literal.
    def enterLiteral(self, ctx:VisualBasic6Parser.LiteralContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#literal.
    def exitLiteral(self, ctx:VisualBasic6Parser.LiteralContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#publicPrivateVisibility.
    def enterPublicPrivateVisibility(self, ctx:VisualBasic6Parser.PublicPrivateVisibilityContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#publicPrivateVisibility.
    def exitPublicPrivateVisibility(self, ctx:VisualBasic6Parser.PublicPrivateVisibilityContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#publicPrivateGlobalVisibility.
    def enterPublicPrivateGlobalVisibility(self, ctx:VisualBasic6Parser.PublicPrivateGlobalVisibilityContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#publicPrivateGlobalVisibility.
    def exitPublicPrivateGlobalVisibility(self, ctx:VisualBasic6Parser.PublicPrivateGlobalVisibilityContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#type_.
    def enterType_(self, ctx:VisualBasic6Parser.Type_Context):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#type_.
    def exitType_(self, ctx:VisualBasic6Parser.Type_Context):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#typeHint.
    def enterTypeHint(self, ctx:VisualBasic6Parser.TypeHintContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#typeHint.
    def exitTypeHint(self, ctx:VisualBasic6Parser.TypeHintContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#visibility.
    def enterVisibility(self, ctx:VisualBasic6Parser.VisibilityContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#visibility.
    def exitVisibility(self, ctx:VisualBasic6Parser.VisibilityContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#ambiguousKeyword.
    def enterAmbiguousKeyword(self, ctx:VisualBasic6Parser.AmbiguousKeywordContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#ambiguousKeyword.
    def exitAmbiguousKeyword(self, ctx:VisualBasic6Parser.AmbiguousKeywordContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#integerLiteral.
    def enterIntegerLiteral(self, ctx:VisualBasic6Parser.IntegerLiteralContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#integerLiteral.
    def exitIntegerLiteral(self, ctx:VisualBasic6Parser.IntegerLiteralContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#octalLiteral.
    def enterOctalLiteral(self, ctx:VisualBasic6Parser.OctalLiteralContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#octalLiteral.
    def exitOctalLiteral(self, ctx:VisualBasic6Parser.OctalLiteralContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#doubleLiteral.
    def enterDoubleLiteral(self, ctx:VisualBasic6Parser.DoubleLiteralContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#doubleLiteral.
    def exitDoubleLiteral(self, ctx:VisualBasic6Parser.DoubleLiteralContext):
        self.depth -= 1
        info("exit", ctx, self.depth)

    # Enter a parse tree produced by VisualBasic6Parser#eCS_ProcedureCall.
    def enterECS_ProcedureCall(self, ctx:VisualBasic6Parser.ECS_ProcedureCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#eCS_ProcedureCall.
    def exitECS_ProcedureCall(self, ctx:VisualBasic6Parser.ECS_ProcedureCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#eCS_MemberProcedureCall.
    def enterECS_MemberProcedureCall(self, ctx:VisualBasic6Parser.ECS_MemberProcedureCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#eCS_MemberProcedureCall.
    def exitECS_MemberProcedureCall(self, ctx:VisualBasic6Parser.ECS_MemberProcedureCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#implicitCallStmt_InBlock.
    def enterImplicitCallStmt_InBlock(self, ctx:VisualBasic6Parser.ImplicitCallStmt_InBlockContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#implicitCallStmt_InBlock.
    def exitImplicitCallStmt_InBlock(self, ctx:VisualBasic6Parser.ImplicitCallStmt_InBlockContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_B_ProcedureCall.
    def enterICS_B_ProcedureCall(self, ctx:VisualBasic6Parser.ICS_B_ProcedureCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_B_ProcedureCall.
    def exitICS_B_ProcedureCall(self, ctx:VisualBasic6Parser.ICS_B_ProcedureCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_B_MemberProcedureCall.
    def enterICS_B_MemberProcedureCall(self, ctx:VisualBasic6Parser.ICS_B_MemberProcedureCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_B_MemberProcedureCall.
    def exitICS_B_MemberProcedureCall(self, ctx:VisualBasic6Parser.ICS_B_MemberProcedureCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#implicitCallStmt_InStmt.
    def enterImplicitCallStmt_InStmt(self, ctx:VisualBasic6Parser.ImplicitCallStmt_InStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#implicitCallStmt_InStmt.
    def exitImplicitCallStmt_InStmt(self, ctx:VisualBasic6Parser.ImplicitCallStmt_InStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_S_VariableOrProcedureCall.
    def enterICS_S_VariableOrProcedureCall(self, ctx:VisualBasic6Parser.ICS_S_VariableOrProcedureCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_S_VariableOrProcedureCall.
    def exitICS_S_VariableOrProcedureCall(self, ctx:VisualBasic6Parser.ICS_S_VariableOrProcedureCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_S_ProcedureOrArrayCall.
    def enterICS_S_ProcedureOrArrayCall(self, ctx:VisualBasic6Parser.ICS_S_ProcedureOrArrayCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_S_ProcedureOrArrayCall.
    def exitICS_S_ProcedureOrArrayCall(self, ctx:VisualBasic6Parser.ICS_S_ProcedureOrArrayCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_S_NestedProcedureCall.
    def enterICS_S_NestedProcedureCall(self, ctx:VisualBasic6Parser.ICS_S_NestedProcedureCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_S_NestedProcedureCall.
    def exitICS_S_NestedProcedureCall(self, ctx:VisualBasic6Parser.ICS_S_NestedProcedureCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_S_MembersCall.
    def enterICS_S_MembersCall(self, ctx:VisualBasic6Parser.ICS_S_MembersCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_S_MembersCall.
    def exitICS_S_MembersCall(self, ctx:VisualBasic6Parser.ICS_S_MembersCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_S_MemberCall.
    def enterICS_S_MemberCall(self, ctx:VisualBasic6Parser.ICS_S_MemberCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_S_MemberCall.
    def exitICS_S_MemberCall(self, ctx:VisualBasic6Parser.ICS_S_MemberCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#iCS_S_DictionaryCall.
    def enterICS_S_DictionaryCall(self, ctx:VisualBasic6Parser.ICS_S_DictionaryCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#iCS_S_DictionaryCall.
    def exitICS_S_DictionaryCall(self, ctx:VisualBasic6Parser.ICS_S_DictionaryCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)




    # Enter a parse tree produced by VisualBasic6Parser#moduleReferences.
    def enterModuleReferences(self, ctx:VisualBasic6Parser.ModuleReferencesContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleReferences.
    def exitModuleReferences(self, ctx:VisualBasic6Parser.ModuleReferencesContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleReference.
    def enterModuleReference(self, ctx:VisualBasic6Parser.ModuleReferenceContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleReference.
    def exitModuleReference(self, ctx:VisualBasic6Parser.ModuleReferenceContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleReferenceValue.
    def enterModuleReferenceValue(self, ctx:VisualBasic6Parser.ModuleReferenceValueContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleReferenceValue.
    def exitModuleReferenceValue(self, ctx:VisualBasic6Parser.ModuleReferenceValueContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleReferenceComponent.
    def enterModuleReferenceComponent(self, ctx:VisualBasic6Parser.ModuleReferenceComponentContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleReferenceComponent.
    def exitModuleReferenceComponent(self, ctx:VisualBasic6Parser.ModuleReferenceComponentContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleHeader.
    def enterModuleHeader(self, ctx:VisualBasic6Parser.ModuleHeaderContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleHeader.
    def exitModuleHeader(self, ctx:VisualBasic6Parser.ModuleHeaderContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleConfig.
    def enterModuleConfig(self, ctx:VisualBasic6Parser.ModuleConfigContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleConfig.
    def exitModuleConfig(self, ctx:VisualBasic6Parser.ModuleConfigContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleConfigElement.
    def enterModuleConfigElement(self, ctx:VisualBasic6Parser.ModuleConfigElementContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleConfigElement.
    def exitModuleConfigElement(self, ctx:VisualBasic6Parser.ModuleConfigElementContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleAttributes.
    def enterModuleAttributes(self, ctx:VisualBasic6Parser.ModuleAttributesContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleAttributes.
    def exitModuleAttributes(self, ctx:VisualBasic6Parser.ModuleAttributesContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleOptions.
    def enterModuleOptions(self, ctx:VisualBasic6Parser.ModuleOptionsContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleOptions.
    def exitModuleOptions(self, ctx:VisualBasic6Parser.ModuleOptionsContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#optionBaseStmt.
    def enterOptionBaseStmt(self, ctx:VisualBasic6Parser.OptionBaseStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#optionBaseStmt.
    def exitOptionBaseStmt(self, ctx:VisualBasic6Parser.OptionBaseStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#optionCompareStmt.
    def enterOptionCompareStmt(self, ctx:VisualBasic6Parser.OptionCompareStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#optionCompareStmt.
    def exitOptionCompareStmt(self, ctx:VisualBasic6Parser.OptionCompareStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#optionExplicitStmt.
    def enterOptionExplicitStmt(self, ctx:VisualBasic6Parser.OptionExplicitStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#optionExplicitStmt.
    def exitOptionExplicitStmt(self, ctx:VisualBasic6Parser.OptionExplicitStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#optionPrivateModuleStmt.
    def enterOptionPrivateModuleStmt(self, ctx:VisualBasic6Parser.OptionPrivateModuleStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#optionPrivateModuleStmt.
    def exitOptionPrivateModuleStmt(self, ctx:VisualBasic6Parser.OptionPrivateModuleStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleBody.
    def enterModuleBody(self, ctx:VisualBasic6Parser.ModuleBodyContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleBody.
    def exitModuleBody(self, ctx:VisualBasic6Parser.ModuleBodyContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleBodyElement.
    def enterModuleBodyElement(self, ctx:VisualBasic6Parser.ModuleBodyElementContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleBodyElement.
    def exitModuleBodyElement(self, ctx:VisualBasic6Parser.ModuleBodyElementContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#controlProperties.
    def enterControlProperties(self, ctx:VisualBasic6Parser.ControlPropertiesContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#controlProperties.
    def exitControlProperties(self, ctx:VisualBasic6Parser.ControlPropertiesContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#cp_Properties.
    def enterCp_Properties(self, ctx:VisualBasic6Parser.Cp_PropertiesContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#cp_Properties.
    def exitCp_Properties(self, ctx:VisualBasic6Parser.Cp_PropertiesContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#cp_SingleProperty.
    def enterCp_SingleProperty(self, ctx:VisualBasic6Parser.Cp_SinglePropertyContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#cp_SingleProperty.
    def exitCp_SingleProperty(self, ctx:VisualBasic6Parser.Cp_SinglePropertyContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#cp_PropertyName.
    def enterCp_PropertyName(self, ctx:VisualBasic6Parser.Cp_PropertyNameContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#cp_PropertyName.
    def exitCp_PropertyName(self, ctx:VisualBasic6Parser.Cp_PropertyNameContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#cp_PropertyValue.
    def enterCp_PropertyValue(self, ctx:VisualBasic6Parser.Cp_PropertyValueContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#cp_PropertyValue.
    def exitCp_PropertyValue(self, ctx:VisualBasic6Parser.Cp_PropertyValueContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#cp_NestedProperty.
    def enterCp_NestedProperty(self, ctx:VisualBasic6Parser.Cp_NestedPropertyContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#cp_NestedProperty.
    def exitCp_NestedProperty(self, ctx:VisualBasic6Parser.Cp_NestedPropertyContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#cp_ControlType.
    def enterCp_ControlType(self, ctx:VisualBasic6Parser.Cp_ControlTypeContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#cp_ControlType.
    def exitCp_ControlType(self, ctx:VisualBasic6Parser.Cp_ControlTypeContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#cp_ControlIdentifier.
    def enterCp_ControlIdentifier(self, ctx:VisualBasic6Parser.Cp_ControlIdentifierContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#cp_ControlIdentifier.
    def exitCp_ControlIdentifier(self, ctx:VisualBasic6Parser.Cp_ControlIdentifierContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#moduleBlock.
    def enterModuleBlock(self, ctx:VisualBasic6Parser.ModuleBlockContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#moduleBlock.
    def exitModuleBlock(self, ctx:VisualBasic6Parser.ModuleBlockContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#attributeStmt.
    def enterAttributeStmt(self, ctx:VisualBasic6Parser.AttributeStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#attributeStmt.
    def exitAttributeStmt(self, ctx:VisualBasic6Parser.AttributeStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#block.
    def enterBlock(self, ctx:VisualBasic6Parser.BlockContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#block.
    def exitBlock(self, ctx:VisualBasic6Parser.BlockContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#blockStmt.
    def enterBlockStmt(self, ctx:VisualBasic6Parser.BlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#blockStmt.
    def exitBlockStmt(self, ctx:VisualBasic6Parser.BlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#appActivateStmt.
    def enterAppActivateStmt(self, ctx:VisualBasic6Parser.AppActivateStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#appActivateStmt.
    def exitAppActivateStmt(self, ctx:VisualBasic6Parser.AppActivateStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#beepStmt.
    def enterBeepStmt(self, ctx:VisualBasic6Parser.BeepStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#beepStmt.
    def exitBeepStmt(self, ctx:VisualBasic6Parser.BeepStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#chDirStmt.
    def enterChDirStmt(self, ctx:VisualBasic6Parser.ChDirStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#chDirStmt.
    def exitChDirStmt(self, ctx:VisualBasic6Parser.ChDirStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#chDriveStmt.
    def enterChDriveStmt(self, ctx:VisualBasic6Parser.ChDriveStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#chDriveStmt.
    def exitChDriveStmt(self, ctx:VisualBasic6Parser.ChDriveStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#closeStmt.
    def enterCloseStmt(self, ctx:VisualBasic6Parser.CloseStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#closeStmt.
    def exitCloseStmt(self, ctx:VisualBasic6Parser.CloseStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#constStmt.
    def enterConstStmt(self, ctx:VisualBasic6Parser.ConstStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#constStmt.
    def exitConstStmt(self, ctx:VisualBasic6Parser.ConstStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#constSubStmt.
    def enterConstSubStmt(self, ctx:VisualBasic6Parser.ConstSubStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#constSubStmt.
    def exitConstSubStmt(self, ctx:VisualBasic6Parser.ConstSubStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#dateStmt.
    def enterDateStmt(self, ctx:VisualBasic6Parser.DateStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#dateStmt.
    def exitDateStmt(self, ctx:VisualBasic6Parser.DateStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#declareStmt.
    def enterDeclareStmt(self, ctx:VisualBasic6Parser.DeclareStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#declareStmt.
    def exitDeclareStmt(self, ctx:VisualBasic6Parser.DeclareStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#deftypeStmt.
    def enterDeftypeStmt(self, ctx:VisualBasic6Parser.DeftypeStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#deftypeStmt.
    def exitDeftypeStmt(self, ctx:VisualBasic6Parser.DeftypeStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#deleteSettingStmt.
    def enterDeleteSettingStmt(self, ctx:VisualBasic6Parser.DeleteSettingStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#deleteSettingStmt.
    def exitDeleteSettingStmt(self, ctx:VisualBasic6Parser.DeleteSettingStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#doLoopStmt.
    def enterDoLoopStmt(self, ctx:VisualBasic6Parser.DoLoopStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#doLoopStmt.
    def exitDoLoopStmt(self, ctx:VisualBasic6Parser.DoLoopStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#endStmt.
    def enterEndStmt(self, ctx:VisualBasic6Parser.EndStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#endStmt.
    def exitEndStmt(self, ctx:VisualBasic6Parser.EndStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#enumerationStmt.
    def enterEnumerationStmt(self, ctx:VisualBasic6Parser.EnumerationStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#enumerationStmt.
    def exitEnumerationStmt(self, ctx:VisualBasic6Parser.EnumerationStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#enumerationStmt_Constant.
    def enterEnumerationStmt_Constant(self, ctx:VisualBasic6Parser.EnumerationStmt_ConstantContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#enumerationStmt_Constant.
    def exitEnumerationStmt_Constant(self, ctx:VisualBasic6Parser.EnumerationStmt_ConstantContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#eraseStmt.
    def enterEraseStmt(self, ctx:VisualBasic6Parser.EraseStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#eraseStmt.
    def exitEraseStmt(self, ctx:VisualBasic6Parser.EraseStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#errorStmt.
    def enterErrorStmt(self, ctx:VisualBasic6Parser.ErrorStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#errorStmt.
    def exitErrorStmt(self, ctx:VisualBasic6Parser.ErrorStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#eventStmt.
    def enterEventStmt(self, ctx:VisualBasic6Parser.EventStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#eventStmt.
    def exitEventStmt(self, ctx:VisualBasic6Parser.EventStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)

    # Enter a parse tree produced by VisualBasic6Parser#exitStmt.
    def enterExitStmt(self, ctx:VisualBasic6Parser.ExitStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#exitStmt.
    def exitExitStmt(self, ctx:VisualBasic6Parser.ExitStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)

    # Enter a parse tree produced by VisualBasic6Parser#getStmt.
    def enterGetStmt(self, ctx:VisualBasic6Parser.GetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#getStmt.
    def exitGetStmt(self, ctx:VisualBasic6Parser.GetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#goSubStmt.
    def enterGoSubStmt(self, ctx:VisualBasic6Parser.GoSubStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#goSubStmt.
    def exitGoSubStmt(self, ctx:VisualBasic6Parser.GoSubStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#goToStmt.
    def enterGoToStmt(self, ctx:VisualBasic6Parser.GoToStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#goToStmt.
    def exitGoToStmt(self, ctx:VisualBasic6Parser.GoToStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#inlineIfThenElse.
    def enterInlineIfThenElse(self, ctx:VisualBasic6Parser.InlineIfThenElseContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#inlineIfThenElse.
    def exitInlineIfThenElse(self, ctx:VisualBasic6Parser.InlineIfThenElseContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#blockIfThenElse.
    def enterBlockIfThenElse(self, ctx:VisualBasic6Parser.BlockIfThenElseContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#blockIfThenElse.
    def exitBlockIfThenElse(self, ctx:VisualBasic6Parser.BlockIfThenElseContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#ifBlockStmt.
    def enterIfBlockStmt(self, ctx:VisualBasic6Parser.IfBlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#ifBlockStmt.
    def exitIfBlockStmt(self, ctx:VisualBasic6Parser.IfBlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#ifConditionStmt.
    def enterIfConditionStmt(self, ctx:VisualBasic6Parser.IfConditionStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#ifConditionStmt.
    def exitIfConditionStmt(self, ctx:VisualBasic6Parser.IfConditionStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#ifElseIfBlockStmt.
    def enterIfElseIfBlockStmt(self, ctx:VisualBasic6Parser.IfElseIfBlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#ifElseIfBlockStmt.
    def exitIfElseIfBlockStmt(self, ctx:VisualBasic6Parser.IfElseIfBlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#ifElseBlockStmt.
    def enterIfElseBlockStmt(self, ctx:VisualBasic6Parser.IfElseBlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#ifElseBlockStmt.
    def exitIfElseBlockStmt(self, ctx:VisualBasic6Parser.IfElseBlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#implementsStmt.
    def enterImplementsStmt(self, ctx:VisualBasic6Parser.ImplementsStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#implementsStmt.
    def exitImplementsStmt(self, ctx:VisualBasic6Parser.ImplementsStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#inputStmt.
    def enterInputStmt(self, ctx:VisualBasic6Parser.InputStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#inputStmt.
    def exitInputStmt(self, ctx:VisualBasic6Parser.InputStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#killStmt.
    def enterKillStmt(self, ctx:VisualBasic6Parser.KillStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#killStmt.
    def exitKillStmt(self, ctx:VisualBasic6Parser.KillStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#letStmt.
    def enterLetStmt(self, ctx:VisualBasic6Parser.LetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#letStmt.
    def exitLetStmt(self, ctx:VisualBasic6Parser.LetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#lineInputStmt.
    def enterLineInputStmt(self, ctx:VisualBasic6Parser.LineInputStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#lineInputStmt.
    def exitLineInputStmt(self, ctx:VisualBasic6Parser.LineInputStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#loadStmt.
    def enterLoadStmt(self, ctx:VisualBasic6Parser.LoadStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#loadStmt.
    def exitLoadStmt(self, ctx:VisualBasic6Parser.LoadStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#lockStmt.
    def enterLockStmt(self, ctx:VisualBasic6Parser.LockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#lockStmt.
    def exitLockStmt(self, ctx:VisualBasic6Parser.LockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#lsetStmt.
    def enterLsetStmt(self, ctx:VisualBasic6Parser.LsetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#lsetStmt.
    def exitLsetStmt(self, ctx:VisualBasic6Parser.LsetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#macroIfThenElseStmt.
    def enterMacroIfThenElseStmt(self, ctx:VisualBasic6Parser.MacroIfThenElseStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#macroIfThenElseStmt.
    def exitMacroIfThenElseStmt(self, ctx:VisualBasic6Parser.MacroIfThenElseStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#macroIfBlockStmt.
    def enterMacroIfBlockStmt(self, ctx:VisualBasic6Parser.MacroIfBlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#macroIfBlockStmt.
    def exitMacroIfBlockStmt(self, ctx:VisualBasic6Parser.MacroIfBlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#macroElseIfBlockStmt.
    def enterMacroElseIfBlockStmt(self, ctx:VisualBasic6Parser.MacroElseIfBlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#macroElseIfBlockStmt.
    def exitMacroElseIfBlockStmt(self, ctx:VisualBasic6Parser.MacroElseIfBlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#macroElseBlockStmt.
    def enterMacroElseBlockStmt(self, ctx:VisualBasic6Parser.MacroElseBlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#macroElseBlockStmt.
    def exitMacroElseBlockStmt(self, ctx:VisualBasic6Parser.MacroElseBlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#midStmt.
    def enterMidStmt(self, ctx:VisualBasic6Parser.MidStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#midStmt.
    def exitMidStmt(self, ctx:VisualBasic6Parser.MidStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#mkdirStmt.
    def enterMkdirStmt(self, ctx:VisualBasic6Parser.MkdirStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#mkdirStmt.
    def exitMkdirStmt(self, ctx:VisualBasic6Parser.MkdirStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#nameStmt.
    def enterNameStmt(self, ctx:VisualBasic6Parser.NameStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#nameStmt.
    def exitNameStmt(self, ctx:VisualBasic6Parser.NameStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#onErrorStmt.
    def enterOnErrorStmt(self, ctx:VisualBasic6Parser.OnErrorStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#onErrorStmt.
    def exitOnErrorStmt(self, ctx:VisualBasic6Parser.OnErrorStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#onGoToStmt.
    def enterOnGoToStmt(self, ctx:VisualBasic6Parser.OnGoToStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#onGoToStmt.
    def exitOnGoToStmt(self, ctx:VisualBasic6Parser.OnGoToStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#onGoSubStmt.
    def enterOnGoSubStmt(self, ctx:VisualBasic6Parser.OnGoSubStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#onGoSubStmt.
    def exitOnGoSubStmt(self, ctx:VisualBasic6Parser.OnGoSubStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#openStmt.
    def enterOpenStmt(self, ctx:VisualBasic6Parser.OpenStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#openStmt.
    def exitOpenStmt(self, ctx:VisualBasic6Parser.OpenStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#outputList.
    def enterOutputList(self, ctx:VisualBasic6Parser.OutputListContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#outputList.
    def exitOutputList(self, ctx:VisualBasic6Parser.OutputListContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#outputList_Expression.
    def enterOutputList_Expression(self, ctx:VisualBasic6Parser.OutputList_ExpressionContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#outputList_Expression.
    def exitOutputList_Expression(self, ctx:VisualBasic6Parser.OutputList_ExpressionContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#printStmt.
    def enterPrintStmt(self, ctx:VisualBasic6Parser.PrintStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#printStmt.
    def exitPrintStmt(self, ctx:VisualBasic6Parser.PrintStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#propertyGetStmt.
    def enterPropertyGetStmt(self, ctx:VisualBasic6Parser.PropertyGetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#propertyGetStmt.
    def exitPropertyGetStmt(self, ctx:VisualBasic6Parser.PropertyGetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#propertySetStmt.
    def enterPropertySetStmt(self, ctx:VisualBasic6Parser.PropertySetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#propertySetStmt.
    def exitPropertySetStmt(self, ctx:VisualBasic6Parser.PropertySetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#propertyLetStmt.
    def enterPropertyLetStmt(self, ctx:VisualBasic6Parser.PropertyLetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#propertyLetStmt.
    def exitPropertyLetStmt(self, ctx:VisualBasic6Parser.PropertyLetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#putStmt.
    def enterPutStmt(self, ctx:VisualBasic6Parser.PutStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#putStmt.
    def exitPutStmt(self, ctx:VisualBasic6Parser.PutStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#raiseEventStmt.
    def enterRaiseEventStmt(self, ctx:VisualBasic6Parser.RaiseEventStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#raiseEventStmt.
    def exitRaiseEventStmt(self, ctx:VisualBasic6Parser.RaiseEventStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#randomizeStmt.
    def enterRandomizeStmt(self, ctx:VisualBasic6Parser.RandomizeStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#randomizeStmt.
    def exitRandomizeStmt(self, ctx:VisualBasic6Parser.RandomizeStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#redimStmt.
    def enterRedimStmt(self, ctx:VisualBasic6Parser.RedimStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#redimStmt.
    def exitRedimStmt(self, ctx:VisualBasic6Parser.RedimStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#redimSubStmt.
    def enterRedimSubStmt(self, ctx:VisualBasic6Parser.RedimSubStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#redimSubStmt.
    def exitRedimSubStmt(self, ctx:VisualBasic6Parser.RedimSubStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#resetStmt.
    def enterResetStmt(self, ctx:VisualBasic6Parser.ResetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#resetStmt.
    def exitResetStmt(self, ctx:VisualBasic6Parser.ResetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#resumeStmt.
    def enterResumeStmt(self, ctx:VisualBasic6Parser.ResumeStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#resumeStmt.
    def exitResumeStmt(self, ctx:VisualBasic6Parser.ResumeStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#returnStmt.
    def enterReturnStmt(self, ctx:VisualBasic6Parser.ReturnStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#returnStmt.
    def exitReturnStmt(self, ctx:VisualBasic6Parser.ReturnStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#rmdirStmt.
    def enterRmdirStmt(self, ctx:VisualBasic6Parser.RmdirStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#rmdirStmt.
    def exitRmdirStmt(self, ctx:VisualBasic6Parser.RmdirStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#rsetStmt.
    def enterRsetStmt(self, ctx:VisualBasic6Parser.RsetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#rsetStmt.
    def exitRsetStmt(self, ctx:VisualBasic6Parser.RsetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#savepictureStmt.
    def enterSavepictureStmt(self, ctx:VisualBasic6Parser.SavepictureStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#savepictureStmt.
    def exitSavepictureStmt(self, ctx:VisualBasic6Parser.SavepictureStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#saveSettingStmt.
    def enterSaveSettingStmt(self, ctx:VisualBasic6Parser.SaveSettingStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#saveSettingStmt.
    def exitSaveSettingStmt(self, ctx:VisualBasic6Parser.SaveSettingStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#seekStmt.
    def enterSeekStmt(self, ctx:VisualBasic6Parser.SeekStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#seekStmt.
    def exitSeekStmt(self, ctx:VisualBasic6Parser.SeekStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#selectCaseStmt.
    def enterSelectCaseStmt(self, ctx:VisualBasic6Parser.SelectCaseStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#selectCaseStmt.
    def exitSelectCaseStmt(self, ctx:VisualBasic6Parser.SelectCaseStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#sC_Case.
    def enterSC_Case(self, ctx:VisualBasic6Parser.SC_CaseContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#sC_Case.
    def exitSC_Case(self, ctx:VisualBasic6Parser.SC_CaseContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#caseCondElse.
    def enterCaseCondElse(self, ctx:VisualBasic6Parser.CaseCondElseContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#caseCondElse.
    def exitCaseCondElse(self, ctx:VisualBasic6Parser.CaseCondElseContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#caseCondExpr.
    def enterCaseCondExpr(self, ctx:VisualBasic6Parser.CaseCondExprContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#caseCondExpr.
    def exitCaseCondExpr(self, ctx:VisualBasic6Parser.CaseCondExprContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#caseCondExprIs.
    def enterCaseCondExprIs(self, ctx:VisualBasic6Parser.CaseCondExprIsContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#caseCondExprIs.
    def exitCaseCondExprIs(self, ctx:VisualBasic6Parser.CaseCondExprIsContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#caseCondExprValue.
    def enterCaseCondExprValue(self, ctx:VisualBasic6Parser.CaseCondExprValueContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#caseCondExprValue.
    def exitCaseCondExprValue(self, ctx:VisualBasic6Parser.CaseCondExprValueContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#caseCondExprTo.
    def enterCaseCondExprTo(self, ctx:VisualBasic6Parser.CaseCondExprToContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#caseCondExprTo.
    def exitCaseCondExprTo(self, ctx:VisualBasic6Parser.CaseCondExprToContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#sendkeysStmt.
    def enterSendkeysStmt(self, ctx:VisualBasic6Parser.SendkeysStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#sendkeysStmt.
    def exitSendkeysStmt(self, ctx:VisualBasic6Parser.SendkeysStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#setattrStmt.
    def enterSetattrStmt(self, ctx:VisualBasic6Parser.SetattrStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#setattrStmt.
    def exitSetattrStmt(self, ctx:VisualBasic6Parser.SetattrStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#setStmt.
    def enterSetStmt(self, ctx:VisualBasic6Parser.SetStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#setStmt.
    def exitSetStmt(self, ctx:VisualBasic6Parser.SetStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#stopStmt.
    def enterStopStmt(self, ctx:VisualBasic6Parser.StopStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#stopStmt.
    def exitStopStmt(self, ctx:VisualBasic6Parser.StopStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)




    # Enter a parse tree produced by VisualBasic6Parser#timeStmt.
    def enterTimeStmt(self, ctx:VisualBasic6Parser.TimeStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#timeStmt.
    def exitTimeStmt(self, ctx:VisualBasic6Parser.TimeStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#typeStmt.
    def enterTypeStmt(self, ctx:VisualBasic6Parser.TypeStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#typeStmt.
    def exitTypeStmt(self, ctx:VisualBasic6Parser.TypeStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#typeStmt_Element.
    def enterTypeStmt_Element(self, ctx:VisualBasic6Parser.TypeStmt_ElementContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#typeStmt_Element.
    def exitTypeStmt_Element(self, ctx:VisualBasic6Parser.TypeStmt_ElementContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#typeOfStmt.
    def enterTypeOfStmt(self, ctx:VisualBasic6Parser.TypeOfStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#typeOfStmt.
    def exitTypeOfStmt(self, ctx:VisualBasic6Parser.TypeOfStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#unloadStmt.
    def enterUnloadStmt(self, ctx:VisualBasic6Parser.UnloadStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#unloadStmt.
    def exitUnloadStmt(self, ctx:VisualBasic6Parser.UnloadStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#unlockStmt.
    def enterUnlockStmt(self, ctx:VisualBasic6Parser.UnlockStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#unlockStmt.
    def exitUnlockStmt(self, ctx:VisualBasic6Parser.UnlockStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsAssign.
    def enterVsAssign(self, ctx:VisualBasic6Parser.VsAssignContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsAssign.
    def exitVsAssign(self, ctx:VisualBasic6Parser.VsAssignContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsNot.
    def enterVsNot(self, ctx:VisualBasic6Parser.VsNotContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsNot.
    def exitVsNot(self, ctx:VisualBasic6Parser.VsNotContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsStruct.
    def enterVsStruct(self, ctx:VisualBasic6Parser.VsStructContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsStruct.
    def exitVsStruct(self, ctx:VisualBasic6Parser.VsStructContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsMultDiv.
    def enterVsMultDiv(self, ctx:VisualBasic6Parser.VsMultDivContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsMultDiv.
    def exitVsMultDiv(self, ctx:VisualBasic6Parser.VsMultDivContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsTypeOf.
    def enterVsTypeOf(self, ctx:VisualBasic6Parser.VsTypeOfContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsTypeOf.
    def exitVsTypeOf(self, ctx:VisualBasic6Parser.VsTypeOfContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsICS.
    def enterVsICS(self, ctx:VisualBasic6Parser.VsICSContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsICS.
    def exitVsICS(self, ctx:VisualBasic6Parser.VsICSContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsXor.
    def enterVsXor(self, ctx:VisualBasic6Parser.VsXorContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsXor.
    def exitVsXor(self, ctx:VisualBasic6Parser.VsXorContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsAddSub.
    def enterVsAddSub(self, ctx:VisualBasic6Parser.VsAddSubContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsAddSub.
    def exitVsAddSub(self, ctx:VisualBasic6Parser.VsAddSubContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsAnd.
    def enterVsAnd(self, ctx:VisualBasic6Parser.VsAndContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsAnd.
    def exitVsAnd(self, ctx:VisualBasic6Parser.VsAndContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsPow.
    def enterVsPow(self, ctx:VisualBasic6Parser.VsPowContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsPow.
    def exitVsPow(self, ctx:VisualBasic6Parser.VsPowContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsMod.
    def enterVsMod(self, ctx:VisualBasic6Parser.VsModContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsMod.
    def exitVsMod(self, ctx:VisualBasic6Parser.VsModContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsAmp.
    def enterVsAmp(self, ctx:VisualBasic6Parser.VsAmpContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsAmp.
    def exitVsAmp(self, ctx:VisualBasic6Parser.VsAmpContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsAddressOf.
    def enterVsAddressOf(self, ctx:VisualBasic6Parser.VsAddressOfContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsAddressOf.
    def exitVsAddressOf(self, ctx:VisualBasic6Parser.VsAddressOfContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsNew.
    def enterVsNew(self, ctx:VisualBasic6Parser.VsNewContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsNew.
    def exitVsNew(self, ctx:VisualBasic6Parser.VsNewContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsPlusMinus.
    def enterVsPlusMinus(self, ctx:VisualBasic6Parser.VsPlusMinusContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsPlusMinus.
    def exitVsPlusMinus(self, ctx:VisualBasic6Parser.VsPlusMinusContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsIDiv.
    def enterVsIDiv(self, ctx:VisualBasic6Parser.VsIDivContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsIDiv.
    def exitVsIDiv(self, ctx:VisualBasic6Parser.VsIDivContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsOr.
    def enterVsOr(self, ctx:VisualBasic6Parser.VsOrContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsOr.
    def exitVsOr(self, ctx:VisualBasic6Parser.VsOrContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsLiteral.
    def enterVsLiteral(self, ctx:VisualBasic6Parser.VsLiteralContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsLiteral.
    def exitVsLiteral(self, ctx:VisualBasic6Parser.VsLiteralContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsEqv.
    def enterVsEqv(self, ctx:VisualBasic6Parser.VsEqvContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsEqv.
    def exitVsEqv(self, ctx:VisualBasic6Parser.VsEqvContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsImp.
    def enterVsImp(self, ctx:VisualBasic6Parser.VsImpContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsImp.
    def exitVsImp(self, ctx:VisualBasic6Parser.VsImpContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsComp.
    def enterVsComp(self, ctx:VisualBasic6Parser.VsCompContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsComp.
    def exitVsComp(self, ctx:VisualBasic6Parser.VsCompContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#vsMid.
    def enterVsMid(self, ctx:VisualBasic6Parser.VsMidContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#vsMid.
    def exitVsMid(self, ctx:VisualBasic6Parser.VsMidContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#variableStmt.
    def enterVariableStmt(self, ctx:VisualBasic6Parser.VariableStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#variableStmt.
    def exitVariableStmt(self, ctx:VisualBasic6Parser.VariableStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#variableListStmt.
    def enterVariableListStmt(self, ctx:VisualBasic6Parser.VariableListStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#variableListStmt.
    def exitVariableListStmt(self, ctx:VisualBasic6Parser.VariableListStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#variableSubStmt.
    def enterVariableSubStmt(self, ctx:VisualBasic6Parser.VariableSubStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#variableSubStmt.
    def exitVariableSubStmt(self, ctx:VisualBasic6Parser.VariableSubStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#whileWendStmt.
    def enterWhileWendStmt(self, ctx:VisualBasic6Parser.WhileWendStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#whileWendStmt.
    def exitWhileWendStmt(self, ctx:VisualBasic6Parser.WhileWendStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#widthStmt.
    def enterWidthStmt(self, ctx:VisualBasic6Parser.WidthStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#widthStmt.
    def exitWidthStmt(self, ctx:VisualBasic6Parser.WidthStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#withStmt.
    def enterWithStmt(self, ctx:VisualBasic6Parser.WithStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#withStmt.
    def exitWithStmt(self, ctx:VisualBasic6Parser.WithStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#writeStmt.
    def enterWriteStmt(self, ctx:VisualBasic6Parser.WriteStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#writeStmt.
    def exitWriteStmt(self, ctx:VisualBasic6Parser.WriteStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#explicitCallStmt.
    def enterExplicitCallStmt(self, ctx:VisualBasic6Parser.ExplicitCallStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#explicitCallStmt.
    def exitExplicitCallStmt(self, ctx:VisualBasic6Parser.ExplicitCallStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)



    # Enter a parse tree produced by VisualBasic6Parser#argsCall.
    def enterArgsCall(self, ctx:VisualBasic6Parser.ArgsCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#argsCall.
    def exitArgsCall(self, ctx:VisualBasic6Parser.ArgsCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#argCall.
    def enterArgCall(self, ctx:VisualBasic6Parser.ArgCallContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#argCall.
    def exitArgCall(self, ctx:VisualBasic6Parser.ArgCallContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#dictionaryCallStmt.
    def enterDictionaryCallStmt(self, ctx:VisualBasic6Parser.DictionaryCallStmtContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#dictionaryCallStmt.
    def exitDictionaryCallStmt(self, ctx:VisualBasic6Parser.DictionaryCallStmtContext):
        self.depth -= 1
        info("exit", ctx, self.depth)




    # Enter a parse tree produced by VisualBasic6Parser#subscripts.
    def enterSubscripts(self, ctx:VisualBasic6Parser.SubscriptsContext):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#subscripts.
    def exitSubscripts(self, ctx:VisualBasic6Parser.SubscriptsContext):
        self.depth -= 1
        info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#subscript_.
    def enterSubscript_(self, ctx:VisualBasic6Parser.Subscript_Context):
        self.depth += 1
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#subscript_.
    def exitSubscript_(self, ctx:VisualBasic6Parser.Subscript_Context):
        self.depth -= 1
        info("exit", ctx, self.depth)
