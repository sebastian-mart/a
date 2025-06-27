import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.io.File

interface Command{
    suspend fun execute()
}
class subMaxim(var hm:HashMap<Int,Int>):Command{
    override suspend fun execute(){
        var max=0
        for((k,v) in hm){
            if(max!! < v){
                max=v
            }
        }
        println("Nr maxim $max")
    }
}

class subMinim(var hm:HashMap<Int,Int>):Command{
    override suspend fun execute(){
        var max=10000000
        for((k,v) in hm){
            if(max!! > v){
                max=v
            }
        }
        println("Nr minim $max")
    }
}
class subAp(var hm:HashMap<Int,Int>):Command{
    override suspend fun execute() {
        val res = mutableMapOf<Int, Int>()
        for ((k, v) in hm) {
            if (res[v] == null) {
                res[v] = 0
            } else {
                val x = res[v]
                if (x != null) {
                    res[v] = x + 1
                }
            }
        }
        println(res)
    }
}
class subElim(var hm:HashMap<Int,Int>):Command{
    override suspend fun execute() {
        val res= mutableMapOf<Int,Int>()
        for((k,v) in hm){
            if (res[v]==null){
                res[v]=1
            }
            else{
//                hm.remove(k)
                println("cheia $k eliminata")
            }
        }
    }
}

class Invoker(val commands:MutableList<Command>){
    fun setCommand(c:Command){
        commands.add(c)
    }
    suspend fun execCommands()= coroutineScope {
        commands.forEach(){
            launch {
                it.execute()
            }
        }
    }
}

fun main()= runBlocking {
    val file= File("file.txt")
    val content=file.readLines().map { it.toInt() }.toList()
    val hm= hashMapOf<Int,Int>()
    for (i in 0 until content.size-1 step 2)
    {

        hm[content[i]]=content[i+1]
    }
    val a=subAp(hm)
    val b=subElim(hm)
    val c=subMaxim(hm)
    val d=subMinim(hm)
    val inv=Invoker(mutableListOf())
    println(hm)
    inv.apply {
        setCommand(a)
        setCommand(b)
        setCommand(c)
        setCommand(d)
    }
    inv.execCommands()

}
