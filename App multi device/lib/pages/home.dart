import 'package:flutter/material.dart';
import 'package:web_tst/pages/cadastro.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
          padding: const EdgeInsets.only(
            top: 30,
            left: 50,
            right: 50,
          ),
          color: Colors.white,
          child: GridView.extent(
            maxCrossAxisExtent: 150,
            padding: EdgeInsets.all(5),
            mainAxisSpacing: 3,
            crossAxisSpacing: 4,
            children: [
              SizedBox(
                width: 128,
                height: 128,
              ),
              SizedBox(
                width: 128,
                height: 128,
                child: Image.asset("img/yasmin.png"),
              ),
              SizedBox(
                width: 128,
                height: 128,
              ),
              Container(
                width: 100,
                height: 100,
                color: Colors.teal,
                child: TextButton(
                  autofocus: true,
                  child: Text(
                    "Cadastro \n     de \n  Cliente",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize: 20,
                    ),
                  ),
                  onPressed: () {
                    Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const Cadastro(),
                        ));
                  },
                ),
              ),
              Container(
                width: 100,
                height: 100,
                color: Colors.teal,
                child: TextButton(
                  child: Text(
                    "Cadastro \n     de \n  Cliente",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize: 20,
                    ),
                  ),
                  onPressed: () {},
                ),
              ),
              Container(
                width: 100,
                height: 100,
                color: Colors.teal,
                child: TextButton(
                  child: Text(
                    "Cadastro \n     de \n  Cliente",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize: 20,
                    ),
                  ),
                  onPressed: () {},
                ),
              )
            ],
          )),
    );
  }
}
