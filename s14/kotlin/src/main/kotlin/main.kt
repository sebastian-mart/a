import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import org.jsoup.select.Elements
import java.io.File

fun save(link:String){
    val a= mutableListOf<Document>()
    val doc = Jsoup.connect(link).get()
    val images = doc.select("img").eachAttr("src").forEach{
//        a.add(Jsoup.connect(it).get())
        println(it)
    }
}

fun main(){
    save("https://ro.wikipedia.org/wiki/Nicu%C8%99or_Dan")
}