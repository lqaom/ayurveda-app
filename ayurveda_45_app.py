import streamlit as st

# ============================================================
# アーユルヴェーダ・プラクリティチェック 45問
# 15問 × 3ドーシャ / 各問 1〜5点 / 各ドーシャ 75点満点
#
# 判定ルール
# ・最も点数の高いドーシャを基本タイプとする
# ・45点以上のドーシャが2種類以上 → 複合体質
# ・3種類とも45点以上 → トリドーシャ
#
# ※研究・設計用のプロトタイプです。
# ============================================================

QUESTIONS = ['動作が素早く、早口で、歩くのも人より速い。', '新しいことを覚えるのが早いが、忘れるのも早い。', '好奇心が強く、何事にも興味を示すが、長続きしない。', '体型はやせている。また、もともとやせ型である。', '手足の静脈が浮き出てよく見える。', '便秘しがちである。', '何か決めるときに、くよくよしがちで決まらない。', 'お腹にガスがたまりやすく、おならが多い。', '元来冷え性で手足が冷たい。寒さを感じやすい。', '座っていても手足や体をいつも動かしている。', '関節がポキポキなることが多い。', '歯の大きさが不揃いで、歯並びもよくない。', '特に冬は、肌がかさつきやすい。', '新しい環境にたやすくとけ込める。', 'お金を儲けるのが早いが、浪費するのも早い。', '自分を主張し、頭脳的、知的でリーダーに向いている。', '汗っかきで夏が苦手である。', '大食漢で、お腹がすくと機嫌が悪い。', '気が短いほうで、イライラしやすく怒りっぽい。', '話し方や行動に無駄がなく、雄弁家といわれる。', '若白髪、若ハゲやシワが若い頃から目立つ。', '冷たい飲み物や食物を好む。', '顔色や肌の色の赤みや黄色みが強い。', '大便が毎日2回以上あり、便は柔らかいことが多い。', '皮膚にホクロやそばかすが多い。', '知的で鋭い目つきをしている。', '日に当たると日焼けしやすい。', '完璧主義者で、人にもきびしい。話し方がきつい。', '目が充血しやすい。', '胸やけや口内炎がよく起こる。', '生まれつきがっちりして体型が大きく、腕力が強い。', '肥満しやすく、腕や足の血管が見えにくい。', '食事を抜いても我慢できる。', '毛髪が黒くて年齢以上にふさふさしている。', 'どこでもよく眠れる。', '肌が柔らかくなめらかで、色白である。', '歯が白くて大きさが揃っており、虫歯も少ない。', '激しい運動や労働によく耐えることができる。', '歩行や食べ方がゆっくりしている。', 'イライラすることは少なく、集中力がある。', '覚えるのは遅いが、いったん覚えると忘れにくい。', 'ひっこみ思案で、恥ずかしがり屋。', '湿気が多くて寒い気候が苦手で、すぐに鼻水が出る。', '食物に興味が強く、食事によくお金を使う。', '心が穏やかで怒ることは少ない。']

DOSHAS = ["ヴァータ", "ピッタ", "カパ"]
QUESTION_DOSHA = ['ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ヴァータ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'ピッタ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ', 'カパ']

OPTIONS = {
    5: "5：とても当てはまる",
    4: "4：まあまあ当てはまる",
    3: "3：どちらともいえない",
    2: "2：あまり当てはまらない",
    1: "1：まったく当てはまらない",
}


def calculate_scores(answers):
    scores = {d: 0 for d in DOSHAS}

    for i, answer in enumerate(answers):
        dosha = QUESTION_DOSHA[i]
        scores[dosha] += answer

    return scores


def get_result(scores):
    # 45点以上のドーシャが2つ以上なら複合体質
    over_45 = [d for d in DOSHAS if scores[d] >= 45]

    if len(over_45) >= 2:
        if len(over_45) == 3:
            result = "トリドーシャ"
        else:
            # 点数順に並べる
            over_45.sort(key=lambda d: scores[d], reverse=True)
            result = "・".join(over_45) + "複合タイプ"
        return result

    # 45点以上が1つ以下なら、最高点を基本タイプ
    max_score = max(scores.values())
    highest = [d for d in DOSHAS if scores[d] == max_score]

    if len(highest) == 1:
        return highest[0] + "タイプ"

    # 45点未満同士で同点の場合
    return "・".join(highest) + "タイプ"


def main():
    st.set_page_config(
        page_title="アーユルヴェーダ・プラクリティ診断",
        page_icon="🌿",
        layout="centered",
    )

    st.title("🌿 アーユルヴェーダ・プラクリティ診断")
    st.write("45問の質問から、ヴァータ・ピッタ・カパの傾向を点数化します。")

    st.info(
        "回答は「5＝とても当てはまる」から「1＝まったく当てはまらない」です。"
    )

    # 回答を保持する
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    with st.form("diagnosis_form"):
        st.subheader("45問に回答してください")

        for i, question in enumerate(QUESTIONS):
            q_num = i + 1

            # 15問ごとに区切る
            if q_num == 1:
                st.markdown("### Ⅰ｜ヴァータに関する質問")
            elif q_num == 16:
                st.markdown("### Ⅱ｜ピッタに関する質問")
            elif q_num == 31:
                st.markdown("### Ⅲ｜カパに関する質問")

            answer = st.radio(
                f"{q_num}. {question}",
                options=list(OPTIONS.keys()),
                format_func=lambda x: OPTIONS[x],
                index=None,
                key=f"q_{q_num}",
                horizontal=False,
            )

        submitted = st.form_submit_button(
            "診断結果を見る",
            use_container_width=True,
        )

    if submitted:
        missing = [
            i + 1
            for i in range(len(QUESTIONS))
            if st.session_state.get(f"q_{i + 1}") is None
        ]

        if missing:
            st.error(
                f"未回答の質問があります。{len(missing)}問残っています。"
                f"（質問番号：{', '.join(map(str, missing))}）"
            )
            return

        answers = [
            st.session_state[f"q_{i + 1}"]
            for i in range(len(QUESTIONS))
        ]

        scores = calculate_scores(answers)
        result = get_result(scores)

        st.session_state.scores = scores
        st.session_state.result = result
        st.session_state.answers = answers

    # 結果表示
    if "result" in st.session_state:
        st.divider()
        st.header("診断結果")

        scores = st.session_state.scores
        result = st.session_state.result

        st.success(f"あなたのプラクリティは「{result}」です。")

        st.subheader("ドーシャ別スコア")

        cols = st.columns(3)
        for col, dosha in zip(cols, DOSHAS):
            with col:
                st.metric(
                    dosha,
                    f"{scores[dosha]} / 75点",
                )

        st.subheader("判定の仕組み")

        over_45 = [d for d in DOSHAS if scores[d] >= 45]

        if len(over_45) >= 2:
            if len(over_45) == 3:
                st.write("45点以上のドーシャが3種類あります → トリドーシャ")
            else:
                st.write(
                    "45点以上のドーシャが2種類以上あります → 複合体質"
                )
        else:
            st.write(
                "最も点数の高いドーシャをプラクリティとしています。"
            )

        # 設計研究用に、回答と採点の対応を確認できるようにする
        with st.expander("採点内訳を確認する"):
            for i, answer in enumerate(st.session_state.answers):
                st.write(
                    f"Q{i + 1}｜{QUESTION_DOSHA[i]}｜{answer}点｜"
                    f"{QUESTIONS[i]}"
                )

        st.caption(
            "※この診断は今回の建築設計・研究用に作成したプロトタイプです。"
        )


if __name__ == "__main__":
    main()
