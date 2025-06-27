import kotlinx.coroutines.awaitAll
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.lang.StringBuilder

class CollectionFunctor<K,V>(val hm:MutableMap<K,V>) {
    suspend fun map(function: (V) -> V): CollectionFunctor<K, V> {
        val result = mutableMapOf<K, V>()
        for ((k, v) in hm) {
            result[k] = function(v)
        }
        return CollectionFunctor(result)
    }
}
fun String.toPascalCase(): String {
    return this
        .split(" ", "-", "_")  // Split by spaces, hyphens, or underscores
        .joinToString("") { word ->
            word.replaceFirstChar { it.uppercase() }
        }
}


fun main(): Unit = runBlocking {

    launch {
        val a= mutableMapOf<Int,String>()
        a[1]="mama tata "
        a[2]="a b c"
        a[3]="d e f "
        val b=CollectionFunctor(a).map{
            "Test"+it
        }.map{
            it.toPascalCase()
        }

        println(b.hm)
    }
}