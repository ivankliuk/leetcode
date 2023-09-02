object Solution {

    val capitalLetters: Set[Char] = Set('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    def toLowerCase(s: String): String =
        s.map {
             c => if (capitalLetters.contains(c)) (c.toInt + 32).toChar else c
        }
}
