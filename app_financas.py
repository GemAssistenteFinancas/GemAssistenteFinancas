import streamlit as st

# --- Configuração Geral da Página ---
st.set_page_config(layout="wide") # Deixa a página mais larga para melhor visualização

st.title("💎 Gem Assistente de Finanças")
st.subheader("Seu Guia para Renda Fixa Segura")

# 1. Definimos as Abas
tab1, tab2 = st.tabs(["🔎 Análise Detalhada de Produto", "💰 Simulação e Regras de Ouro"])

# --- LÓGICA DA ABA 1: ANÁLISE DETALHADA DE PRODUTO (Versão 1) ---
with tab1:
    st.header("Análise Rápida de Segurança (Risco, Prazo, Lucro)")
    st.write("Use esta aba se você tiver as informações claras do seu gerente.")

    # Área de Inputs
    with st.container(border=True):
        nome_do_investimento = st.text_input("1. Qual o NOME do produto? (Ex: CDB, LCI, Poupança):").upper()
        taxa_str = st.text_input("2. Quanto promete pagar? (Ex: 100, 90, 85 - se for % do CDI):")
        
        col_fgc, col_liq = st.columns(2)
        with col_fgc:
            tem_fgc = st.radio("3. Tem garantia do FGC (o seguro)?", ('Sim', 'Não', 'Não sei'), key='fgc_radio').upper()
        with col_liq:
            liquidez_diaria = st.radio("4. Resgate a qualquer momento? (Liquidez Diária)", ('Sim', 'Não', 'Não sei'), key='liq_radio').upper()

    # --- Análise e Resultados da Aba 1 ---
    if nome_do_investimento and taxa_str and taxa_str.replace('.', '').isdigit():
        st.markdown("---")
        st.subheader("✅ RESULTADO DA ANÁLISE")

        # A. Análise da SEGURANÇA (FGC)
        if tem_fgc == 'SIM':
            st.success("✅ SEGURANÇA: Ótimo! Este produto tem a garantia do FGC (o seguro).")
        elif nome_do_investimento == 'POUPANÇA':
             st.success("✅ SEGURANÇA: A Poupança tem garantia do governo.")
        else:
            st.warning("⚠️ SEGURANÇA: Atenção! Se não tem FGC ou você não sabe, o risco é maior.")

        # B. Análise da LIQUIDEZ (Tempo)
        if liquidez_diaria == 'SIM':
            st.info("💧 LIQUIDEZ: Perfeito! Ideal para RESERVA DE EMERGÊNCIA.")
        else:
            st.error("⏳ LIQUIDEZ: Cuidado! Se o resgate não for diário, este dinheiro ficará 'PRESO' até o vencimento. Não use para reserva de emergência!")

        # C. Análise do IMPOSTO DE RENDA
        if nome_do_investimento in ['LCI', 'LCA']:
            st.write("✨ IMPOSTO: **Excelente!** LCI e LCA são **ISENTOS de Imposto de Renda**.")
        elif nome_do_investimento == 'CDB':
            st.write("💲 IMPOSTO: CDB paga Imposto de Renda. O lucro que você vê será um pouco menor após o desconto.")

        # D. Análise do LUCRO (Rentabilidade)
        try:
            lucro = float(taxa_str)
            if lucro >= 100:
                st.success(f"💰 LUCRO: A taxa de **{lucro}% do CDI** é EXCELENTE!")
            elif lucro >= 90:
                st.info(f"💰 LUCRO: A taxa de **{lucro}% do CDI** é BOA.")
            else:
                st.warning(f"📉 LUCRO: A taxa de **{lucro}% do CDI** é BAIXA. Busque opções melhores.")
        except ValueError:
            st.warning("⚠️ LUCRO: Por favor, insira a porcentagem do CDI corretamente.")


# --- LÓGICA DA ABA 2: SIMULAÇÃO E REGRAS DE OURO (Versão 2 - com Dicionário) ---
with tab2:
    st.header("Se Arme com o Mínimo Aceitável!")
    st.write("Use esta aba para saber o que você deve aceitar do seu gerente ANTES de conversar com ele.")

    # Adicionando o Dicionário Rápido com Expander
    st.markdown("---")
    with st.expander("📚 **Dicionário Rápido para Iniciantes**"):
        st.markdown("""
        - **CDB (Certificado de Depósito Bancário):** Você empresta dinheiro para o banco. Paga Imposto de Renda.
        - **LCI/LCA (Letra de Crédito):** Você empresta dinheiro para o banco financiar o setor imobiliário/agro. **Não paga Imposto de Renda (Isento).**
        - **FGC (Fundo Garantidor de Créditos):** É o **seguro** que protege seu dinheiro (CDB, LCI, LCA) em caso de falência do banco, limitado a R$ 250 mil por CPF.
        - **Liquidez Diária:** Significa que você pode resgatar o dinheiro a **qualquer momento** sem perder a rentabilidade do período. Essencial para Reserva de Emergência.
        """)

    # 1. ENTRADAS NECESSÁRIAS
    with st.container(border=True):
        cdi_estimado_str = st.text_input("1. Qual a Taxa Selic/CDI ESTIMADA por ano (Ex: 10.50)? (Procure o valor atual na internet)", key='cdi_input')
        objetivo_input = st.radio("2. Para que é o dinheiro?", ('Reserva de Emergência', 'Objetivo de Longo Prazo'), key='obj_radio')
        
    if cdi_estimado_str:
        try:
            taxa_cdi = float(cdi_estimado_str)
            
            # 2. DEFINIÇÃO DAS REGRAS
            cdb_ideal = 100
            lci_ideal = 85 
            
            st.markdown("---")
            st.subheader("🌟 REGRAS DE OURO DO INVESTIDOR INICIANTE")

            # RECOMENDAÇÃO 1: LIQUIDEZ
            if objetivo_input == 'Reserva de Emergência':
                st.error("🚨 **1. LIQUIDEZ:** Para Reserva de Emergência, EXIJA Liquidez Diária e FGC. Dinheiro preso NÃO é reserva!")
            else:
                st.success("✅ **1. LIQUIDEZ:** Para Longo Prazo, é aceitável ter o dinheiro 'preso' se a taxa for MUITO melhor.")

            # RECOMENDAÇÃO 2: TAXAS MÍNIMAS (O poder de dizer 'Não')
            st.markdown("\n💰 **2. TAXAS MÍNIMAS (O seu poder de negociação):**")
            st.info(f"   - **CDB (Com IR):** EXIJA MÍNIMO de **{cdb_ideal}% do CDI**.")
            st.info(f"   - **LCI/LCA (Isento de IR):** EXIJA MÍNIMO de **{lci_ideal}% do CDI** (Isso é o equivalente a 100% do CDI após Impostos).")

            # RECOMENDAÇÃO 3: ALERTA DE RISCO
            st.warning("🛡️ **3. ALERTA DE RISCO:** Não use dinheiro de reserva em produtos sem FGC ou Renda Variável (Ações, Criptomoedas)!")
            
            # RECOMENDAÇÃO 4: RESUMO DE SEGURANÇA
            st.markdown("⭐ **4. RESUMO:** Se o gerente não responder **CLARAMENTE** sobre FGC e Liquidez Diária, Diga **NÃO** e peça uma opção simples e transparente.")

        except ValueError:
            st.error("⚠️ Por favor, insira a taxa CDI como um número válido (Ex: 10.50).")