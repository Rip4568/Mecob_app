# Generated by Django 4.2.2 on 2023-06-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcessoPessoa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=45, null=True)),
                ('url', models.CharField(blank=True, max_length=300, null=True)),
                ('post', models.TextField(blank=True, null=True)),
                ('texto_get', models.TextField(blank=True, null=True)),
                ('request', models.TextField(blank=True, null=True)),
                ('nivel_permissao', models.IntegerField(blank=True, null=True)),
                ('cookie', models.TextField(blank=True, null=True)),
                ('ehlogin', models.CharField(blank=True, db_column='ehLogin', max_length=45, null=True)),
                ('caminho_arquivo', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'acesso_pessoa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alertas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=1000)),
                ('visualizado', models.CharField(blank=True, max_length=1, null=True)),
                ('data_alerta', models.DateTimeField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('concluido', models.CharField(blank=True, max_length=50, null=True)),
                ('dt_concluido', models.DateTimeField(blank=True, null=True)),
                ('dt_prazo', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'alertas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nm_arq', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_arq', models.DateTimeField(blank=True, null=True)),
                ('tp_arq', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_envio_banco', models.DateTimeField(blank=True, null=True)),
                ('log', models.TextField(blank=True, null=True)),
                ('dt_processamento', models.DateTimeField(blank=True, null=True)),
                ('origem', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'arquivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoletosAvulso',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dt_boleto', models.DateField()),
                ('descricao', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'boletos_avulso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContratoLote',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vl_lote', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'contrato_lote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContratoParcelas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nu_parcela', models.IntegerField(blank=True, null=True)),
                ('dt_vencimento', models.DateField(blank=True, null=True)),
                ('dt_pagto', models.DateField(blank=True, null=True)),
                ('vl_parcela', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_correcao_monetaria', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_juros', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_pagto', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_juros_pagto', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_honorarios', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_taxa', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_multa', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('vl_corrigido', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('liquidada_no_cadastro', models.CharField(blank=True, max_length=45, null=True)),
                ('simulada', models.CharField(blank=True, max_length=45, null=True)),
                ('dt_vencimento_original', models.DateField(blank=True, null=True)),
                ('nu_linha_remessa', models.IntegerField(blank=True, null=True)),
                ('nu_linha_retorno', models.CharField(blank=True, max_length=45, null=True)),
                ('dt_credito', models.DateField(blank=True, null=True)),
                ('dt_processo_pagto', models.DateTimeField(blank=True, null=True)),
                ('tratar_ted', models.IntegerField(blank=True, null=True)),
                ('fl_negativada', models.CharField(blank=True, max_length=45, null=True)),
                ('motivo_zerado', models.CharField(blank=True, max_length=150, null=True)),
                ('observacao_zerado', models.CharField(blank=True, max_length=2000, null=True)),
                ('fl_acao_judicial', models.CharField(blank=True, max_length=45, null=True)),
                ('dt_atualizacao_monetaria', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contrato_parcelas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=500, null=True)),
                ('dt_contrato', models.DateField(blank=True, null=True)),
                ('vl_contrato', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('nu_parcelas', models.IntegerField(blank=True, null=True)),
                ('vl_entrada', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tp_contrato', models.CharField(blank=True, max_length=50, null=True)),
                ('dt_inclusao', models.DateTimeField(blank=True, null=True)),
                ('honor_adimp', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('honor_inadimp', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('parcela_primeiro_pagto', models.IntegerField(blank=True, null=True)),
                ('juros', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('dt_primeira_parcela', models.DateField(blank=True, null=True)),
                ('instrucao', models.TextField(blank=True, null=True)),
                ('termo_percentual_contrato', models.CharField(blank=True, max_length=100, null=True)),
                ('termo_descricao_lote', models.TextField(blank=True, null=True)),
                ('termo_descricao_pagto', models.TextField(blank=True, null=True)),
                ('termo_local_data', models.CharField(blank=True, max_length=500, null=True)),
                ('termo_nomes_lote', models.CharField(blank=True, max_length=500, null=True)),
                ('tp_contrato_boleto', models.CharField(blank=True, max_length=50, null=True)),
                ('gerar_boleto', models.CharField(blank=True, max_length=45, null=True)),
                ('desconto_total', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('fl_parcelas_zerado', models.CharField(blank=True, max_length=45, null=True)),
                ('dt_parcelas_zerado', models.DateTimeField(blank=True, null=True)),
                ('motivo_zerado', models.CharField(blank=True, max_length=150, null=True)),
                ('observacao_zerado', models.CharField(blank=True, max_length=2000, null=True)),
                ('dt_acao_judicial', models.DateTimeField(blank=True, null=True)),
                ('suspenso', models.CharField(blank=True, max_length=1, null=True)),
                ('dt_suspensao', models.DateField(blank=True, null=True)),
                ('dt_retorno_suspensao', models.DateField(blank=True, null=True)),
                ('repasse', models.CharField(blank=True, max_length=1, null=True)),
                ('status_antes_acordo', models.CharField(blank=True, max_length=45, null=True)),
                ('fiador', models.TextField(blank=True, null=True)),
                ('animal', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contratos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DadosArquivoRetorno',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nosso_numero', models.CharField(blank=True, max_length=45, null=True)),
                ('id_ocorrencia', models.CharField(blank=True, max_length=45, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1000, null=True)),
                ('dt_banco', models.DateField(blank=True, null=True)),
                ('dt_vencimento', models.DateField(blank=True, null=True)),
                ('vl_boleto', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('vl_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('vl_juros', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('dt_credito', models.DateField(blank=True, null=True)),
                ('motivo_ocorrencia', models.CharField(blank=True, max_length=45, null=True)),
                ('nu_linha', models.IntegerField(blank=True, null=True)),
                ('fl_processado', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'dados_arquivo_retorno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=500)),
                ('file', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'documentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=500, null=True)),
                ('dt_evento', models.DateField()),
                ('tipo', models.CharField(db_collation='utf8mb3_general_ci', db_comment='(virtual, presencial, online)', max_length=200)),
            ],
            options={
                'db_table': 'eventos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Haras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('contato', models.CharField(blank=True, max_length=500, null=True)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('proprietario_nome', models.CharField(blank=True, max_length=500, null=True)),
                ('proprietario_doc', models.CharField(blank=True, max_length=500, null=True)),
                ('rua', models.CharField(blank=True, max_length=500, null=True)),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('complemento', models.CharField(blank=True, max_length=1000, null=True)),
                ('bairro', models.CharField(blank=True, max_length=200, null=True)),
                ('cidade', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, max_length=200, null=True)),
                ('cep', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'haras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndiceCgj',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dt_indice', models.DateField()),
                ('vl_indice', models.DecimalField(decimal_places=6, max_digits=12)),
            ],
            options={
                'db_table': 'indice_cgj',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LancamentosTed',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tipo', models.CharField(blank=True, max_length=200, null=True)),
                ('obs', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lancamentos_ted',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('num_registro', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_nascimento', models.DateField(blank=True, null=True)),
                ('tipo', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'lotes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=45, unique=True)),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'modulo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ocorrencias',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=500, null=True)),
                ('mensagem', models.TextField(blank=True, null=True)),
                ('data_ocorrencia', models.DateTimeField(blank=True, null=True)),
                ('contratos_id_original', models.IntegerField(blank=True, null=True)),
                ('ligacao_feita', models.CharField(blank=True, max_length=1, null=True)),
                ('promessa_pagamento', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ocorrencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=45, unique=True)),
                ('dt_atualizacao', models.DateTimeField()),
                ('fixo', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'perfil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerfilModulo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('visualizar', models.CharField(blank=True, max_length=45, null=True)),
                ('adicionar', models.CharField(blank=True, max_length=45, null=True)),
                ('editar', models.CharField(blank=True, max_length=45, null=True)),
                ('conceder', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'perfil_modulo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_nascimento', models.DateField(blank=True, null=True)),
                ('cpf_cnpj', models.CharField(blank=True, max_length=45, null=True)),
                ('rg', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('saltdb', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_ativo', models.DateTimeField(blank=True, null=True)),
                ('apelido', models.CharField(blank=True, max_length=45, null=True)),
                ('dt_inclusao', models.DateTimeField(blank=True, null=True)),
                ('rua', models.CharField(blank=True, max_length=200, null=True)),
                ('numero', models.CharField(blank=True, max_length=45, null=True)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=45, null=True)),
                ('cep', models.CharField(blank=True, max_length=45, null=True)),
                ('celular', models.CharField(blank=True, max_length=45, null=True)),
                ('site', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('sobre', models.CharField(blank=True, max_length=1000, null=True)),
                ('eh_leiloeiro', models.CharField(max_length=45)),
                ('eh_vendedor', models.CharField(max_length=45)),
                ('eh_comprador', models.CharField(max_length=45)),
                ('eh_user', models.CharField(max_length=45)),
                ('telefone', models.CharField(blank=True, max_length=45, null=True)),
                ('contato', models.CharField(blank=True, max_length=200, null=True)),
                ('eh_admin', models.CharField(max_length=200)),
                ('honor_adimp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('honor_inadimp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=200, null=True)),
                ('supervisor', models.CharField(blank=True, max_length=1, null=True)),
                ('operador', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'pessoas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Protocolos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('protocolo', models.CharField(max_length=12)),
                ('dt_registro', models.DateTimeField()),
                ('cad_pessoa', models.BigIntegerField(blank=True, null=True)),
                ('vendedor', models.CharField(blank=True, max_length=100, null=True)),
                ('vendedor_id', models.BigIntegerField(blank=True, null=True)),
                ('comprador', models.CharField(blank=True, max_length=100, null=True)),
                ('comprador_id', models.BigIntegerField(blank=True, null=True)),
                ('evento', models.CharField(blank=True, max_length=500, null=True)),
                ('evento_id', models.BigIntegerField(blank=True, null=True)),
                ('produto', models.CharField(blank=True, max_length=100, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('dt_parcela', models.DateField()),
                ('nr_parcela', models.IntegerField()),
                ('prazo', models.DateField()),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('setor', models.CharField(blank=True, max_length=45, null=True)),
                ('setor_trans', models.DateTimeField(blank=True, null=True)),
                ('trans_pessoa', models.BigIntegerField(blank=True, null=True)),
                ('finalizado', models.DateTimeField(blank=True, null=True)),
                ('finalizado_pessoa', models.BigIntegerField(blank=True, null=True)),
                ('finalizado_motivo', models.CharField(blank=True, max_length=500, null=True)),
                ('contrato_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('enable', models.IntegerField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('dt_contrato', models.DateField(blank=True, null=True)),
                ('dt_digitalizado', models.DateField(blank=True, null=True)),
                ('ct_verifica', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'protocolos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProtocolosEventos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('setor', models.CharField(max_length=45)),
                ('ocorrencia', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField()),
                ('pessoas_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'protocolos_eventos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProtocolosServicos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('tipo', models.CharField(max_length=100)),
                ('enviado', models.DateField(blank=True, null=True)),
                ('recebido', models.DateField(blank=True, null=True)),
                ('digitalizado', models.DateField(blank=True, null=True)),
                ('fisico', models.DateField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('dt_registro', models.DateTimeField()),
                ('dt_atualizacao', models.DateTimeField(blank=True, null=True)),
                ('pessoa_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('enable', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'protocolos_servicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProtocolosSetor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('setor', models.CharField(max_length=45)),
                ('data', models.DateTimeField()),
                ('pessoas_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'protocolos_setor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RodizioClientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoas_id', models.IntegerField(blank=True, null=True)),
                ('tp_contrato', models.CharField(blank=True, max_length=45, null=True)),
                ('vendedor_id', models.IntegerField(blank=True, null=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('id_rodizio', models.IntegerField(blank=True, null=True)),
                ('ativo', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'rodizio_clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SendMail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('assunto', models.CharField(blank=True, max_length=1000, null=True)),
                ('mensagem', models.TextField(blank=True, null=True)),
                ('email_dest', models.CharField(blank=True, max_length=200, null=True)),
                ('nome_dest', models.CharField(blank=True, max_length=200, null=True)),
                ('email_reply', models.CharField(blank=True, max_length=200, null=True)),
                ('nome_reply', models.CharField(blank=True, max_length=200, null=True)),
                ('prioridade', models.IntegerField()),
            ],
            options={
                'db_table': 'send_mail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SendMailDestinatarios',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('enviado', models.IntegerField()),
            ],
            options={
                'db_table': 'send_mail_destinatarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teds',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dt_inclusao', models.DateTimeField(blank=True, null=True)),
                ('dt_ted', models.DateField(blank=True, null=True)),
                ('vl_ted', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('status_ted', models.IntegerField(blank=True, null=True)),
                ('banco', models.IntegerField(blank=True, null=True)),
                ('agencia', models.IntegerField(blank=True, null=True)),
                ('dv_agencia', models.CharField(blank=True, max_length=45, null=True)),
                ('conta', models.IntegerField(blank=True, null=True)),
                ('dv_conta', models.CharField(blank=True, max_length=45, null=True)),
                ('nu_linha_remessa', models.IntegerField(blank=True, null=True)),
                ('nu_linha_retorno_previa', models.IntegerField(blank=True, null=True)),
                ('nu_linha_retorno_processamento', models.IntegerField(blank=True, null=True)),
                ('nu_linha_retorno_consolidado', models.IntegerField(blank=True, null=True)),
                ('del_domc_bancario', models.IntegerField(blank=True, null=True)),
                ('log_zerar', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'teds',
                'managed': False,
            },
        ),
    ]
